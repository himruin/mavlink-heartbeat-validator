# MAVLink HEARTBEAT Message Parameters
- https://mavlink.io/en/messages/common.html#HEARTBEAT
- https://mavlink.io/en/services/heartbeat.html

## type - uint8_t
Vehicle type. Enum values:
- 0 = Generic
- 1 = Fixed Wing Aircraft
- 2 = Quadrotor
- Reference: `MAV_TYPE_*` constants

## autopilot - uint8_t
Autopilot system type. Enum values:
- 0 = Generic
- 3 = PX4 Autopilot
- 4 = ArduPilot
- 5 = Openpilot
- Reference: `MAV_AUTOPILOT_*` constants

## base_mode - uint8_t
System mode flags. Bitmask of:
- Bit 0: MAV_MODE_FLAG_ARMED
- Bit 1: MAV_MODE_FLAG_GUIDED
- Bit 2: MAV_MODE_FLAG_STABILIZE_ENABLED
- Bit 3: MAV_MODE_FLAG_HIL_ENABLED
- Bit 4: MAV_MODE_FLAG_MANUAL_INPUT_ENABLED
- Bit 5: MAV_MODE_FLAG_SAFETY_ARMED

## custom_mode - uint32_t
Custom mode value (free-form, autopilot-specific). Not a standard enum.
Examples (ArduPilot):
- 0 = Stabilize
- 2 = Alt Hold
- 3 = Auto

## system_status - uint8_t
System health/readiness state. Enum values:
- 0 = Uninit
- 1 = Boot
- 2 = Calibrating
- 3 = Standby
- 4 = Active
- 5 = Critical
- Reference: `MAV_STATE_*` constants
