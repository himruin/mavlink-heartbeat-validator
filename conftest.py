import pytest
from mavlink_test_utils import heartbeat_msg


@pytest.fixture
def drone_factory():
    """factory for creating drone state dicts with heartbeat fields and overrideable defaults"""

    def _factory(lat=0.0, lon=0.0, altitude=0.0, on_ground=True, **heartbeat_kwargs):
        hb = heartbeat_msg(**heartbeat_kwargs)
        return {**hb, "lat": lat, "lon": lon, "altitude": altitude, "on_ground": on_ground}

    return _factory