import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from pieforhead.topic import TopicAsync


def make_topic(response: dict | None) -> tuple[TopicAsync, Mock]:
    """Make a mock TopicAsync class to return toy data.

    Args:
        response (dict | None): value returned by TopicAsync._client.request()

    Returns:
        tuple[TopicAsync, Mock]: The TopicAsync and the client that were created
    """
    client = Mock()
    client.request = AsyncMock(return_value=response)

    return TopicAsync(client), client


# Ensure parameter passed through
@pytest.mark.parametrize("include_communities", [True, False])
def test_list(include_communities: bool):
    async def run_test():
        response = {"topics": ["Test topic"]}
        topic, client = make_topic(response)

        # Check response
        assert await topic.list(include_communities=include_communities) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="topic/list",
            params={"include_communities": include_communities},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


# Check default value of include_communities
def test_list_defaults():
    async def run_test():
        response = {"topics": ["Test topic"]}
        topic, client = make_topic(response)

        # Check response
        assert await topic.list() == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="topic/list",
            params={"include_communities": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


# Make sure None is returned when request error is suppressed and just returns None
def test_list_handles_none():
    async def run_test():
        topic, client = make_topic(None)

        # Check response
        assert await topic.list() is None

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="topic/list",
            params={"include_communities": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())
