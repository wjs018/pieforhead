from unittest.mock import Mock

from pieforhead.feed import Feed


def make_feed(response: dict | None) -> tuple[Feed, Mock]:
    client = Mock()
    client.request.return_value = response
    return Feed(client), client


def test_get_by_id():
    response = {"id": 42}
    feed, client = make_feed(response)

    # Check response
    assert feed.get(feed_id=42) == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="feed", params={"id": 42})


def test_get_by_name():
    response = {"id": 42}
    feed, client = make_feed(response)

    # Check response
    assert feed.get(feed_name="test_feed@site.tld") == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="feed", params={"name": "test_feed@site.tld"})


def test_create_all_fields():
    response = {"id": 42}
    feed, client = make_feed(response)

    # Check response
    assert (
        feed.create(
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
    client.request.assert_called_once_with(
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


def test_create_few_fields():
    response = {"id": 42}
    feed, client = make_feed(response)

    # Check response
    assert feed.create(name="test", title="Test feed") is response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="feed",
        data={"name": "test", "title": "Test feed"},
    )


def test_edit_all_fields():
    response = {"id": 42}
    feed, client = make_feed(response)

    # Check response
    assert (
        feed.edit(
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
    client.request.assert_called_once_with(
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


def test_edit_nullable_fields():
    response = {"id", 42}
    feed, client = make_feed(response)

    # Check response
    assert (
        feed.edit(
            feed_id=42,
            title="",
            description="",
            icon_url="",
            banner_url="",
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
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


def test_list_defaults():
    response = {"feeds": [{"id": 42}]}
    feed, client = make_feed(response)

    # Check response
    assert feed.list() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="feed/list", params={})


def test_list_params():
    response = {"feeds": [{"id": 42}]}
    feed, client = make_feed(response)

    # Check response
    assert feed.list(include_communities=False, mine_only=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET", endpoint="feed/list", params={"include_communities": False, "mine_only": True}
    )


def test_follow():
    response = {"id", 42}
    feed, client = make_feed(response)

    # Check response
    assert feed.follow(feed_id=42, follow=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="feed/follow",
        data={"feed_id": 42, "follow": False},
    )


def test_delete():
    response = {"id", 42}
    feed, client = make_feed(response)

    # Check response
    assert feed.delete(feed_id=42, deleted=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="feed/delete",
        data={"feed_id": 42, "deleted": True},
    )


def test_subscribe():
    response = {"id", 42}
    feed, client = make_feed(response)

    # Check response
    assert feed.subscribe(feed_id=42, subscribed=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="feed/subscribe",
        data={"feed_id": 42, "subscribe": False},
    )
