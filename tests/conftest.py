import pytest

@pytest.fixture
def mavlink_connection():
    """in-memory MAVlink encoder/decoder"""
    from pymavlink import mavutil
    from io import BytesIO

    encoder = mavutil.mavlink.MAVLink(BytesIO())
    return encoder