"""negative testing of malformed/invalid MAVLink heartbeat message frames"""

import pytest
from pymavlink import mavutil
from io import BytesIO
from mavlink_test_utils import heartbeat_msg


def test_truncated_frame(mavlink_connection):
    """Truncated message returns None — frame incomplete before parsing starts"""
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()

    truncated = raw_bytes[:8]

    decoder = mavutil.mavlink.MAVLink(BytesIO())
    result = decoder.parse_buffer(truncated)
    assert result is None


def test_heartbeat_prefix_corrupted(mavlink_connection, fault_injector):
    """Invalid prefix causes parse failure — byte 0, first thing checked"""
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()

    # corrupt prefix byte (pos 0)
    corrupted = fault_injector(raw_bytes, position=0)

    decoder = mavutil.mavlink.MAVLink(BytesIO())
    with pytest.raises(Exception) as exc:
        decoder.parse_buffer(corrupted)
    assert "invalid mavlink prefix" in str(exc.value).lower()


def test_heartbeat_wrong_message_id(mavlink_connection, fault_injector):
    """Wrong message ID byte is parsed as MAVLink_unknown, not HEARTBEAT"""
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()

    # MAVLink v1 frame: byte 5 is the message ID (HEARTBEAT = 0x00)
    # XOR 0xFF → 0xFF (255), not a valid common dialect message ID
    corrupted = fault_injector(raw_bytes, position=5)

    decoder = mavutil.mavlink.MAVLink(BytesIO())
    messages = decoder.parse_buffer(corrupted)
    assert len(messages) == 1
    assert isinstance(messages[0], mavutil.mavlink.MAVLink_unknown)
    assert messages[0].get_type() != "HEARTBEAT"


def test_corrupted_payload_validation(mavlink_connection, fault_injector):
    """Corrupted payload bytes cause CRC failure — data region bytes 6–14"""
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()

    # corrupt all payload bytes (pos 6-13)
    corrupted = raw_bytes
    for pos in range(6, 14):
        corrupted = fault_injector(corrupted, position=pos)

    decoder = mavutil.mavlink.MAVLink(BytesIO())
    with pytest.raises(Exception) as exc:
        decoder.parse_buffer(corrupted)
    assert "crc" in str(exc.value).lower()


def test_heartbeat_crc_corrupted(mavlink_connection, fault_injector):
    """CRC corruption causes parse failure — last 2 bytes, final integrity check"""
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()

    # corrupt both CRC bytes (pos: CRC1=-2, CRC2=-1)
    corrupted = fault_injector(raw_bytes, position=-2)
    corrupted = fault_injector(corrupted, position=-1)

    decoder = mavutil.mavlink.MAVLink(BytesIO())
    with pytest.raises(Exception) as exc:
        decoder.parse_buffer(corrupted)
    assert "crc" in str(exc.value).lower() or "checksum" in str(exc.value).lower()