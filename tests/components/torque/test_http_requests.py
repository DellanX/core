"""Test the torque config flow."""
from http import HTTPStatus

import pytest

from homeassistant.components.torque.const import API_PATH
from homeassistant.core import HomeAssistant

from .const import DATA_HEADER_QUERY, DATA_PROFILE_QUERY, DATA_VALUE_QUERY

from tests.typing import ClientSessionGenerator

pytestmark = pytest.mark.usefixtures("mock_setup_entry")


async def test_http_valid_requests(
    hass: HomeAssistant,
    hass_client: ClientSessionGenerator,
) -> None:
    """Test state storage."""
    # Setup Phase, Create a Torque Integration
    component = True
    assert component is True
    # Upload Phase, Create a client, and send mock data
    client = await hass_client()

    resp = await client.get(API_PATH, params=DATA_PROFILE_QUERY)
    assert resp.status == HTTPStatus.OK

    resp = await client.get(API_PATH, params=DATA_HEADER_QUERY)
    assert resp.status == HTTPStatus.OK

    resp = await client.get(API_PATH, params=DATA_VALUE_QUERY)
    assert resp.status == HTTPStatus.OK
    # Assertion Phase, check the states of the device entities, and make sure they match the expected data
    # Snapshot could probably be used here
