import pytest
import requests
import responses
from mavlink_test_utils import OPENSKY_URL, SYSTEM_STATUS_TYPES


def _make_state_vector(drone):
    on_ground = drone["on_ground"]
    system_status = (
        SYSTEM_STATUS_TYPES["STANDBY"] if on_ground else SYSTEM_STATUS_TYPES["ACTIVE"]
    )
    return [
        "abc123",  # icao24
        "DRONE01 ",  # callsign
        "Test",  # origin_country
        None,  # time_position
        None,  # last_contact
        drone["lon"],  # longitude
        drone["lat"],  # latitude
        drone["altitude"],  # baro_altitude
        on_ground,  # on_ground
        0.0,  # velocity
        0.0,  # true_track
        0.0,  # vertical_rate
        None,  # sensors
        drone["altitude"],  # geo_altitude
        None,  # squawk
        False,  # spi
        0,  # position_source
        system_status,  # MAVLink system_status
    ]


@pytest.fixture
def http_session():
    return requests.Session()


@pytest.fixture
def mock_opensky(drone_factory):
    drone = drone_factory()
    payload = {
        "time": 1617896720,
        "states": [_make_state_vector(drone)],
    }
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, OPENSKY_URL, json=payload, status=200)
        yield drone  # tests receive the drone dict to assert against
