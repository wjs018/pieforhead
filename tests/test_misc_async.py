import asyncio
from unittest.mock import AsyncMock, Mock

from pieforhead.misc import MiscAsync


def make_misc(response: dict | None, raise_exceptions: bool = True) -> tuple[MiscAsync, Mock]:
    """Make a mock MiscAsync class to return toy data."""
    client = Mock()
    client.request = AsyncMock(return_value=response)
    client.raise_exceptions = raise_exceptions

    return MiscAsync(client), client


def test_search():
    async def run_test():
        response = {"posts": [{"post_id": 42}]}
        misc, client = make_misc(response)

        # Check response
        assert await misc.search(query="test", type_="Posts") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="search",
            params={"q": "test", "type_": "Posts"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_search_optional_params():
    async def run_test():
        response = {"posts": [{"post_id": 42}]}
        misc, client = make_misc(response)

        # Check response
        assert (
            await misc.search(
                query="test",
                type_="Posts",
                limit=10,
                listing_type="All",
                page=2,
                sort="New",
                community_name="python",
                community_id=3,
                minimum_upvotes=5,
                nsfw="false",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="search",
            params={
                "q": "test",
                "type_": "Posts",
                "limit": 10,
                "listing_type": "All",
                "page": 2,
                "sort": "New",
                "community_name": "python",
                "community_id": 3,
                "minimum_upvotes": 5,
                "nsfw": "false",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_search_raising():
    async def run_test():
        # Make sure to return None if request returns None
        misc, client = make_misc(None, raise_exceptions=False)

        # Check response
        assert await misc.search(query="test", type_="Posts") is None

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="search",
            params={"q": "test", "type_": "Posts"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_resolve_object():
    async def run_test():
        response = {"post": {"post_id": 42}}
        misc, client = make_misc(response)

        # Check response
        assert await misc.resolve_object(query="https://site.tld/post/42") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="resolve_object",
            params={"q": "https://site.tld/post/42"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_resolve_object_raising():
    async def run_test():
        # Make sure to return None if request returns None
        misc, client = make_misc(None, raise_exceptions=False)

        # Check response
        assert await misc.resolve_object(query="https://site.tld/post/42") is None

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="resolve_object",
            params={"q": "https://site.tld/post/42"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_federated_instances():
    async def run_test():
        response = {"federated_instances": {"linked": [], "allowed": [], "blocked": []}}
        misc, client = make_misc(response)

        # Check response
        assert await misc.federated_instances() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="federated_instances")

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_federated_instances_raising():
    async def run_test():
        # Make sure to return None if request returns None
        misc, client = make_misc(None, raise_exceptions=False)

        # Check response
        assert await misc.federated_instances() is None

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="federated_instances")

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_suggest_completion():
    async def run_test():
        response = {"result": ["test_user1", "test_user2"]}
        misc, client = make_misc(response)

        # Check response
        assert await misc.suggest_completion(query="@tes") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="suggest_completion",
            params={"q": "@tes"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_suggest_completion_raising():
    async def run_test():
        # Make sure to return None if request returns None
        misc, client = make_misc(None, raise_exceptions=False)

        # Check response
        assert await misc.suggest_completion(query="@tes") is None

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="suggest_completion",
            params={"q": "@tes"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_modlog():
    async def run_test():
        response = {"added": [{"mod_add": {"id": 42}}]}
        misc, client = make_misc(response)

        # Check response
        assert await misc.modlog() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="modlog", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_modlog_non_default_posts():
    async def run_test():
        response = {"removed_posts": [{"mod_remove_post": {"id": 42}}]}
        misc, client = make_misc(response)

        # Check response
        assert (
            await misc.modlog(
                mod_person_id=1,
                community_id=2,
                page=3,
                limit=20,
                type_="ModRemovePost",
                other_person_id=4,
                post_id=5,
                comment_id=6,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="modlog",
            params={
                "mod_person_id": 1,
                "community_id": 2,
                "page": 3,
                "limit": 20,
                "type_": "ModRemovePost",
                "other_person_id": 4,
                "post_id": 5,
                "comment_id": 6,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_modlog_raising():
    async def run_test():
        # Make sure to return None if request returns None
        misc, client = make_misc(None, raise_exceptions=False)

        # Check response
        assert await misc.modlog() is None

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="modlog", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())
