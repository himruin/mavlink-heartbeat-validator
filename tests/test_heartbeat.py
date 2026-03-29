"""positive testing of parsing MAVLink heartbeat message frames"""
import pytest
from conftest import heartbeat_msg, AUTOPILOT_TYPES


def test_parse_valid_heartbeat(mavlink_connection):
    """parse a valid heartbeat frame and check its field values"""
    msg = heartbeat_msg()
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()
    messages = mavlink_connection.parse_buffer(raw_bytes)
    assert messages[0].type == msg["type"]
    assert messages[0].autopilot == msg["autopilot"]
    assert messages[0].base_mode == msg["base_mode"]
    assert messages[0].custom_mode == msg["custom_mode"]
    assert messages[0].system_status == msg["system_status"]


@pytest.mark.parametrize("autopilot", list(AUTOPILOT_TYPES.values()))
def test_autopilot_enum(mavlink_connection, autopilot):
    """check setting of all expected autopilot values"""
    msg = heartbeat_msg(autopilot=autopilot)
    mavlink_connection.heartbeat_send(**msg)
    raw_bytes = mavlink_connection.file.getvalue()
    messages = mavlink_connection.parse_buffer(raw_bytes)
    assert messages[0].autopilot == autopilot


def test_multiple_heartbeats_sequence(mavlink_connection):
    """parse sequentially multiple heartbeats messages"""
    for autopilot in AUTOPILOT_TYPES.values():
        msg = heartbeat_msg(autopilot=autopilot)
        mavlink_connection.heartbeat_send(**msg)

    raw_bytes = mavlink_connection.file.getvalue()
    messages = mavlink_connection.parse_buffer(raw_bytes)
    assert len(messages) >= 3  # All 3 frames parsed
