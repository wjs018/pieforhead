from unittest.mock import Mock

import pytest

from pieforhead.exceptions import NotImplementedError
from pieforhead.site import Site


def make_site(response: dict | None, raise_exceptions: bool = True) -> tuple[Site, Mock]:
    """Make a mock Site class to return toy data.

    Args:
        response (dict | None): value returned by Site._client.request()
        raise_exceptions (bool): whether the client should raise exceptions or not. Defaults to True.

    Returns:
        tuple[Site, Mock]: The Site and the client that were created
    """
    client = Mock()
    client.request.return_value = response
    client.raise_exceptions = raise_exceptions

    return Site(client), client


def test_get_site():
    response = {"site": "Test site"}
    site, client = make_site(response)

    assert site.get() == response  # ensure request was successful
    client.request.assert_called_once_with(method="GET", endpoint="site")  # ensure proper args passed along


def test_site_version():
    response = {"version": "1.2.3"}
    site, client = make_site(response)

    assert site.version() == response  # Ensure proper response
    client.request.assert_called_once_with(method="GET", endpoint="site/version")  # ensure proper args


# Test looks the same for both Site.get and Site.version
@pytest.mark.parametrize("endpoint", ["get", "version"])
def test_get_version_raising(endpoint: str):
    """Ensures that Site.get returns None when the response returns None.

    This should only happen when raise_exceptions=False, so we suppress the errors and just return None.
    """
    site, client = make_site(None)

    # Endpoint to validate request against
    if endpoint == "get":
        request_endpoint = "site"
    elif endpoint == "version":
        request_endpoint = "site/version"

    site_func = getattr(site, endpoint)
    assert site_func() is None  # ensure proper response of None
    client.request.assert_called_once_with(method="GET", endpoint=request_endpoint)  # ensure proper args passed along


# Parameterize the block value to test both cases
@pytest.mark.parametrize("block", [True, False])
def test_site_block(block: bool):
    response = {"blocked": block}
    site, client = make_site(response)

    # Ensure proper response and args
    assert site.block(block=block, instance_id=42) == response
    client.request.assert_called_once_with(
        method="POST",
        endpoint="site/block",
        data={"block": block, "instance_id": 42},
    )


@pytest.mark.parametrize("block", [True, False])
def test_block_raising(block: bool):
    """Ensures that Site.block returns None when the response returns None."""
    site, client = make_site(None)

    assert site.block(block=block, instance_id=42) is None
    client.request.assert_called_once_with(
        method="POST",
        endpoint="site/block",
        data={"block": block, "instance_id": 42},
    )


# Parameterize unimplemented endpoints to iterate through them
@pytest.mark.parametrize("method_name", ["instance_chooser", "instance_chooser_search"])
def test_unimplemented_methods(method_name: str):
    site, _ = make_site({})

    with pytest.raises(NotImplementedError):
        # Make sure custom exception is raised when function invoked
        site_func = getattr(site, method_name)
        site_func()


# Parameterize unimplemented endpoints to iterate through them
@pytest.mark.parametrize("method_name", ["instance_chooser", "instance_chooser_search"])
def test_unimplemented_methods_raising(method_name: str):
    site, client = make_site(None, raise_exceptions=False)

    assert client.raise_exceptions is False  # Ensure attribute is saved to client

    site_func = getattr(site, method_name)
    assert site_func() is None  # Ensure that no exception is raised, just return None
