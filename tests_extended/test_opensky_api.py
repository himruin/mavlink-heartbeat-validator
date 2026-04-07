"""OpenSky Network API tests — schema and MAVLink field mapping validation"""

from mavlink_test_utils import OPENSKY_URL, SYSTEM_STATUS_TYPES


def test_status_code(mock_opensky, http_session):
    resp = http_session.get(OPENSKY_URL)
    assert resp.status_code == 200


def test_response_schema(mock_opensky, http_session):
    resp = http_session.get(OPENSKY_URL)
    data = resp.json()
    assert "time" in data
    assert "states" in data
    assert isinstance(data["states"], list)


def test_state_vector_length(mock_opensky, http_session):
    resp = http_session.get(OPENSKY_URL)
    state_vector = resp.json()["states"][0]
    assert len(state_vector) >= 17


def test_on_ground_maps_to_system_status(mock_opensky, http_session):
    resp = http_session.get(OPENSKY_URL)
    state_vector = resp.json()["states"][0]
    on_ground = state_vector[8]
    system_status = state_vector[17]
    expected = (
        SYSTEM_STATUS_TYPES["STANDBY"] if on_ground else SYSTEM_STATUS_TYPES["ACTIVE"]
    )
    assert system_status == expected
