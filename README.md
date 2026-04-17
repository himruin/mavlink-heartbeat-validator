# MAVLink Heartbeat Validator

Sample project to practice MAVLink protocol testing using pytest framework. MAVLink is structurally similar to automotive serialized protocols — fixed header, typed fields, CRC.

A pytest suite that validates MAVLink HEARTBEAT message parsing using pymavlink's dialect system — pure in-process protocol logic, no hardware, no network.

References:
- [pymavlink Python API](https://mavlink.io/en/mavgen_python/)
- [HEARTBEAT message spec](https://mavlink.io/en/messages/common.html#HEARTBEAT)

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

**`tests/test_heartbeat.py` — positive tests**
- [x] Valid heartbeat parse — all fields asserted
- [x] Parametrized autopilot enum values (GENERIC, PX4, ARDUPILOT, OPENPILOT)
- [x] Multiple heartbeats parsed sequentially from a single buffer

**`tests/test_heartbeat_malformed.py` — negative tests (ordered by frame position)**
- [x] Truncated frame — incomplete bytes return `None` before parsing starts
- [x] Prefix corruption — invalid start byte (pos 0) raises parse error
- [x] Wrong message ID — corrupted ID byte (pos 5) parsed as `MAVLink_unknown`, not `HEARTBEAT`
- [x] Payload corruption — corrupted data bytes (pos 6–13) trigger CRC failure
- [x] CRC corruption — corrupted checksum bytes (pos −2, −1) raise CRC error

## Project Goals

- Demonstrates MAVLink domain knowledge: protocol enums, frame structure, CRC validation
- Clean, focused test organization using pytest
