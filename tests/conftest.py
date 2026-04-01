import pytest
from pymavlink import mavutil
from io import BytesIO

# Enum values from docs/heartbeat.md
AUTOPILOT_TYPES = {
    "GENERIC": 0,
    "PX4": 3,
    "ARDUPILOT": 4,
    "OPENPILOT": 5,
}

SYSTEM_STATUS_TYPES = {
    "UNINIT": 0,
    "BOOT": 1,
    "CALIBRATING": 2,
    "STANDBY": 3,
    "ACTIVE": 4,
    "CRITICAL": 5,
}


def heartbeat_msg(
    type=1,
    autopilot=AUTOPILOT_TYPES["ARDUPILOT"],
    base_mode=209,
    custom_mode=0,
    system_status=SYSTEM_STATUS_TYPES["ACTIVE"],
):
    """factory for creating heartbeat message dicts with overrideable defaults"""
    return {
        "type": type,
        "autopilot": autopilot,
        "base_mode": base_mode,
        "custom_mode": custom_mode,
        "system_status": system_status,
    }


@pytest.fixture
def mavlink_connection():
    """in-memory MAVLink encoder/decoder"""
    return mavutil.mavlink.MAVLink(BytesIO())


@pytest.fixture
def fault_injector():
    """inject a fault into a MAVLink frame by corrupting a specific byte via XOR"""

    def _inject(raw_bytes, position, flip_mask=0xFF):
        corrupted = bytearray(raw_bytes)
        corrupted[position] ^= flip_mask
        return bytes(corrupted)

    return _inject
