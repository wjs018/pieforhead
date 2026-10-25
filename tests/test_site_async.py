import asyncio
from unittest.mock import AsyncMock, Mock

import pytest
import semver

from pieforhead.exceptions import NotImplementedError, SiteException
from pieforhead.site import SiteAsync


def make_site(response: dict) -> tuple[SiteAsync, Mock]:
    """Make a mock SiteAsync class to return toy data.

    Args:
        response (dict): dict that is returned by SiteAsync._client.request()

    Returns:
        tuple[SiteAsync, Mock]: The SiteAsync and the client that were created
    """
    client = Mock()
    client.request = AsyncMock(return_value=response)
    return SiteAsync(client), client


def test_get_site():
    async def run_test():
        response = {"site": "Test site"}
        site, client = make_site(response)

        assert await site.get() == response  # ensure request was successful
        client.request.assert_awaited_once_with(method="GET", endpoint="site")  # ensure proper args passed along

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_site_version():
    async def run_test():
        response = {"version": "1.2.3"}
        site, client = make_site(response)

        assert await site.version() == semver.Version.parse("1.2.3")  # Correct type, value is returned
        client.request.assert_awaited_once_with(method="GET", endpoint="site/version")  # ensure proper args

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_site_exception():
    async def run_test():
        site, client = make_site({"version": "not-a-version"})

        with pytest.raises(SiteException, match="Version not parseable: not-a-version"):
            # Ensure that the custom exception is raised when version can't be parsed
            await site.version()

        client.request.assert_awaited_once_with(method="GET", endpoint="site/version")  # ensure proper args

    # Start the event loop and run the test
    asyncio.run(run_test())


# Parameterize the block value to test both cases
@pytest.mark.parametrize("block", [True, False])
def test_site_block(block: bool):
    async def run_test():
        site, client = make_site({"blocked": block})

        # Ensure proper response and args
        assert await site.block(block=block, instance_id=42) is block
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="site/block",
            data={"block": block, "instance_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


# Parameterize unimplemented endpoints to iterate through them
@pytest.mark.parametrize("method_name", ["instance_chooser", "instance_chooser_search"])
def test_unimplemented_methods(method_name: str):
    async def run_test():
        site, _ = make_site({})

        with pytest.raises(NotImplementedError):
            # Make sure custom exception is raised when function invoked
            site_func = getattr(site, method_name)
            await site_func()

    # Start the event loop and run the test
    asyncio.run(run_test())
