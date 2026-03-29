# MAVLink Heartbeat Validator

Sample project to practice MAVLink protocol testing using pytest framework. MAVLink is structurally similar to automotive serialized protocols — fixed header, typed fields, CRC.

## Project Assumption

A pytest suite that validates MAVLink HEARTBEAT message parsing using pymavlink's dialect system — pure in-process protocol logic, no hardware, no network.

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
- 3 focused test cases: valid parse, magic byte failure, parametrized autopilot enums

## TODO

- [ ] Heartbeat tests: valid parse, magic byte failure, parametrized autopilot enums
- [ ] Malformed frame tests: truncated, wrong message ID, corrupted payload

## Project Goals

- Demonstrate pytest fixture design with pymavlink
- Show domain awareness: MAVLink protocol specifics (enums, checksums, frame structure)
- Clean, focused test organization
