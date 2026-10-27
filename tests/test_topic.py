from unittest.mock import Mock

import pytest

from pieforhead.topic import Topic


def make_topic(response: dict | None) -> tuple[Topic, Mock]:
    """Make a mock Topic class to return toy data.

    Args:
        response (dict | None): value returned by Topic._client.request()

    Returns:
        tuple[Topic, Mock]: The Topic and the client that were created
    """
    client = Mock()
    client.request.return_value = response

    return Topic(client), client


# Ensure parameter passed through
@pytest.mark.parametrize("include_communities", [True, False])
def test_list(include_communities: bool):
    response = {"topics": ["Test topic"]}
    topic, client = make_topic(response)

    # Check response
    assert topic.list(include_communities=include_communities) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="topic/list",
        params={"include_communities": include_communities},
    )


# Check default value of include_communities
def test_list_defaults():
    response = {"topics": ["Test topic"]}
    topic, client = make_topic(response)

    # Check response
    assert topic.list() == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="topic/list",
        params={"include_communities": True},
    )


# Make sure None is returned when request error is suppressed and just returns None
def test_list_handles_none():
    topic, client = make_topic(None)

    # Check response
    assert topic.list() is None

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="topic/list",
        params={"include_communities": True},
    )
