# MAVLink Heartbeat Validator

Sample project to practice MAVLink protocol testing using pytest framework. MAVLink is structurally similar to automotive serialized protocols — fixed header, typed fields, CRC.

## Project Assumption

A pytest suite that validates MAVLink HEARTBEAT message parsing using pymavlink's dialect system — pure in-process protocol logic, no hardware, no network.
Links:
- https://mavlink.io/en/mavgen_python/
- https://mavlink.io/en/messages/common.html#HEARTBEAT

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
pytest -v
```

## Approach

- Generate raw MAVLink HEARTBEAT frames in-process using pymavlink dialect system
- Parse back and assert on decoded fields (type, autopilot, system_status)
- No network, no hardware — pure protocol logic

## Test Coverage

- [x] **Positive tests:** Valid heartbeat parse + parametrized autopilot enum values + multiple heartbeats sequentially
- [x] **Negative tests:** Prefix corruption + CRC corruption

## Future Enhancements Ideas

- [ ] Wrong message ID handling
- [ ] Truncated frame detection
- [ ] Payload integrity validation

## Project Goals

- Testing of drones domain acknowledgment: MAVLink protocol specifics (enums, checksums, frame structure)
- Clean, focused test organization using pytest
