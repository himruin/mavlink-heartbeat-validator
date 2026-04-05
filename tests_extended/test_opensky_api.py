"""OpenSky Network API tests — schema and MAVLink field mapping validation"""

import requests
from conftest import OPENSKY_URL


def test_status_code(mock_opensky, http_session): ...


def test_response_schema(mock_opensky, http_session): ...


def test_state_vector_length(mock_opensky, http_session): ...


def test_on_ground_maps_to_system_status(mock_opensky, http_session): ...