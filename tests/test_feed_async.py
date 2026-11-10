import asyncio
from unittest.mock import AsyncMock, Mock

from pieforhead.feed import FeedAsync


def make_feed(response: dict | None) -> tuple[FeedAsync, Mock]:
    client = Mock()
    client.request = AsyncMock(return_value=response)
    return FeedAsync(client), client


def test_get_by_id():
    async def run_test():
        response = {"id": 42}
        feed, client = make_feed(response)

        # Check response
        assert await feed.get(feed_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="feed", params={"id": 42})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_by_name():
    async def run_test():
        response = {"id": 42}
        feed, client = make_feed(response)

        # Check response
        assert await feed.get(feed_name="test_feed@site.tld") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="feed",
            params={"name": "test_feed@site.tld"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_all_fields():
    async def run_test():
        response = {"id": 42}
        feed, client = make_feed(response)

        # Check response
        assert (
            await feed.create(
                name="test",
                title="Test feed",
                description="Description",
                icon_url="icon.png",
                banner_url="banner.png",
                nsfw=False,
                nsfl=True,
                public=False,
                communities="community1@instance.tld\ncommunity2@instance.tld",
                is_instance_feed=False,
                show_child_posts=False,
                parent_feed_id=2,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="feed",
            data={
                "name": "test",
                "title": "Test feed",
                "description": "Description",
                "icon_url": "icon.png",
                "banner_url": "banner.png",
                "nsfw": False,
                "nsfl": True,
                "public": False,
                "communities": "community1@instance.tld\ncommunity2@instance.tld",
                "is_instance_feed": False,
                "show_child_posts": False,
                "parent_feed_id": 2,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_few_fields():
    async def run_test():
        response = {"id": 42}
        feed, client = make_feed(response)

        # Check response
        assert await feed.create(name="test", title="Test feed") is response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="feed",
            data={"name": "test", "title": "Test feed"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_all_fields():
    async def run_test():
        response = {"id": 42}
        feed, client = make_feed(response)

        # Check response
        assert (
            await feed.edit(
                feed_id=42,
                url="https://instance.tld/f/test",
                title="Testing",
                description="Description",
                icon_url="icon.png",
                banner_url="banner.png",
                nsfw=False,
                nsfl=True,
                public=False,
                communities="community1@instance.tld\ncommunity2@instance.tld",
                is_instance_feed=False,
                show_child_posts=False,
                parent_feed_id=2,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="feed",
            data={
                "feed_id": 42,
                "url": "https://instance.tld/f/test",
                "nsfw": False,
                "nsfl": True,
                "public": False,
                "communities": "community1@instance.tld\ncommunity2@instance.tld",
                "is_instance_feed": False,
                "show_child_posts": False,
                "parent_feed_id": 2,
                "title": "Testing",
                "description": "Description",
                "icon_url": "icon.png",
                "banner_url": "banner.png",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_nullable_fields():
    async def run_test():
        response = {"id", 42}
        feed, client = make_feed(response)

        # Check response
        assert (
            await feed.edit(
                feed_id=42,
                title="",
                description="",
                icon_url="",
                banner_url="",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="feed",
            data={
                "feed_id": 42,
                "title": None,
                "description": None,
                "icon_url": None,
                "banner_url": None,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_defaults():
    async def run_test():
        response = {"feeds": [{"id": 42}]}
        feed, client = make_feed(response)

        # Check response
        assert await feed.list() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="feed/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_params():
    async def run_test():
        response = {"feeds": [{"id": 42}]}
        feed, client = make_feed(response)

        # Check response
        assert await feed.list(include_communities=False, mine_only=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="feed/list",
            params={"include_communities": False, "mine_only": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_follow():
    async def run_test():
        response = {"id", 42}
        feed, client = make_feed(response)

        # Check response
        assert await feed.follow(feed_id=42, follow=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="feed/follow",
            data={"feed_id": 42, "follow": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete():
    async def run_test():
        response = {"id", 42}
        feed, client = make_feed(response)

        # Check response
        assert await feed.delete(feed_id=42, deleted=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="feed/delete",
            data={"feed_id": 42, "deleted": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_subscribe():
    async def run_test():
        response = {"id", 42}
        feed, client = make_feed(response)

        # Check response
        assert await feed.subscribe(feed_id=42, subscribed=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="feed/subscribe",
            data={"feed_id": 42, "subscribe": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())
