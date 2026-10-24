from unittest.mock import Mock

import pytest
import semver

from pieforhead.exceptions import NotImplementedError, SiteException
from pieforhead.site import Site


def make_site(response: dict) -> tuple[Site, Mock]:
    """Make a mock Site class to return toy data.

    Args:
        response (dict): dict that is returned by Site._client.request()

    Returns:
        tuple[Site, Mock]: The Site and the client that were created
    """
    client = Mock()
    client.request.return_value = response
    return Site(client), client


def test_get_site():
    response = {"site": "Test site"}
    site, client = make_site(response)

    assert site.get() == response  # ensure request was successful
    client.request.assert_called_once_with(method="GET", endpoint="site")  # ensure proper args passed along


def test_site_version():
    response = {"version": "1.2.3"}
    site, client = make_site(response)

    assert site.version() == semver.Version.parse("1.2.3")  # Correct type, value is returned
    client.request.assert_called_once_with(method="GET", endpoint="site/version")  # ensure proper args


def test_site_exception():
    site, client = make_site({"version": "not-a-version"})

    with pytest.raises(SiteException, match="Version not parseable: not-a-version"):
        # Ensure that the custom exception is raised when version can't be parsed
        site.version()

    client.request.assert_called_once_with(method="GET", endpoint="site/version")  # ensure proper args


# Parameterize the block value to test both cases
@pytest.mark.parametrize("block", [True, False])
def test_site_block(block: bool):
    site, client = make_site({"blocked": block})

    # Ensure proper response and args
    assert site.block(block=block, instance_id=42) is block
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
