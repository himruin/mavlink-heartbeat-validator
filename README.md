# MAVLink Heartbeat Validator

Sample project to practice MAVLink protocol testing using pytest framework. MAVLink is structurally similar to automotive serialized protocols — fixed header, typed fields, CRC.

A pytest suite that validates MAVLink HEARTBEAT message parsing using pymavlink's dialect system, plus mocked OpenSky Network API integration tests.

References:
- [pymavlink Python API](https://mavlink.io/en/mavgen_python/)
- [HEARTBEAT message spec](https://mavlink.io/en/messages/common.html#HEARTBEAT)
- [OpenSky Network REST API](https://openskynetwork.github.io/opensky-api/rest.html)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
# all tests
pytest -v

# MAVLink protocol tests only
pytest tests/ -v

# OpenSky API tests only
pytest tests_extended/ -v

# exclude live network tests
pytest -m "not integration" -v
```

## Approach

- Generate raw MAVLink HEARTBEAT frames in-process using pymavlink dialect system
- Parse back and assert on decoded fields (type, autopilot, system_status)
- OpenSky API responses mocked with `responses` library — no live network calls

## Test Coverage

**`tests/` — MAVLink protocol (pure in-process)**
- [x] **Positive tests:** Valid heartbeat parse + parametrized autopilot enum values + multiple heartbeats sequentially
- [x] **Negative tests:** Prefix corruption + CRC corruption

**`tests_extended/` — OpenSky Network API (mocked)**
- [x] **Status code:** HTTP 200 response
- [x] **Response schema:** `time` and `states` keys present
- [x] **State vector length:** ≥ 17 fields per state vector
- [x] **Field mapping:** `on_ground` maps correctly to MAVLink `system_status` (`STANDBY`/`ACTIVE`)

## Future Enhancements

- [ ] Wrong message ID handling
- [ ] Truncated frame detection
- [ ] Payload integrity validation

## Project Goals

- Demonstrates MAVLink domain knowledge: protocol enums, frame structure, CRC validation
- OpenSky API field mapping to MAVLink system status
- Clean, focused test organization using pytest
