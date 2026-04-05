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

HEARTBEAT_FIELDS = {"type", "autopilot", "base_mode", "custom_mode", "system_status"}


def heartbeat_msg(
    type=1,
    autopilot=AUTOPILOT_TYPES["ARDUPILOT"],
    base_mode=209,
    custom_mode=0,
    system_status=SYSTEM_STATUS_TYPES["STANDBY"],
):
    """creator for heartbeat message dicts with overrideable defaults"""
    return {
        "type": type,
        "autopilot": autopilot,
        "base_mode": base_mode,
        "custom_mode": custom_mode,
        "system_status": system_status,
    }
