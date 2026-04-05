import pytest
import responses
from mavlink_test_utils import SYSTEM_STATUS_TYPES

OPENSKY_URL = "https://opensky-network.org/api/states/all"

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

