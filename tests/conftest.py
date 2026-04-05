import pytest
from pymavlink import mavutil
from io import BytesIO


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