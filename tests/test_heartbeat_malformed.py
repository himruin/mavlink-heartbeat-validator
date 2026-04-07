"""negative testing of malformed/invalid MAVLink heartbeat message frames"""

import pytest
from pymavlink import mavutil
from io import BytesIO
from mavlink_test_utils import heartbeat_msg


def test_heartbeat_prefix_corrupted(mavlink_connection, fault_injector):
    """Invalid prefix causes parse failure"""
    # create valid frame
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()

    # corrupt prefix byte (pos 0)
    corrupted = fault_injector(raw_bytes, position=0)

    # assert parse failure
    decoder = mavutil.mavlink.MAVLink(BytesIO(corrupted))
    with pytest.raises(Exception) as exc:
        decoder.parse_buffer(corrupted)
    assert "invalid mavlink prefix" in str(exc.value).lower()


def test_heartbeat_crc_corrupted(mavlink_connection, fault_injector):
    """CRC corruption causes parse failure"""
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()

    # corrupt both CRC bytes (pos: CRC1=-2, CRC2=-1)
    corrupted = fault_injector(raw_bytes, position=-2)
    corrupted = fault_injector(corrupted, position=-1)

    # verify parser rejects corrupted CRC
    decoder = mavutil.mavlink.MAVLink(BytesIO(corrupted))
    with pytest.raises(Exception) as exc:
        decoder.parse_buffer(corrupted)
    assert "crc" in str(exc.value).lower() or "checksum" in str(exc.value).lower()
