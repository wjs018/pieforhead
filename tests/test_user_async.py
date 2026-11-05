import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from pieforhead.exceptions import NotImplementedError
from pieforhead.user import UserAsync


def make_user(response: dict | bool | None, raise_exceptions: bool = True) -> tuple[UserAsync, Mock]:
    """Make a mock async User class to return toy data."""
    client = Mock()
    client.request = AsyncMock(return_value=response)
    client.log_in = AsyncMock(return_value=response)
    client.log_out = AsyncMock(return_value=response)
    client.raise_exceptions = raise_exceptions

    return UserAsync(client), client


def test_get_all_params():
    async def run_test():
        response = {"person_view": {"activity_alert": True}}
        user, client = make_user(response)

        # Check response
        assert (
            await user.get(
                person_id=42,
                username="test_user",
                sort="New",
                page=2,
                limit=10,
                community_id=3,
                saved_only=False,
                include_content=True,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="user",
            params={
                "person_id": 42,
                "username": "test_user",
                "sort": "New",
                "page": 2,
                "limit": 10,
                "community_id": 3,
                "saved_only": False,
                "include_content": True,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_defaults():
    async def run_test():
        user, client = make_user(None, raise_exceptions=False)

        # Response is None when request returns None
        assert await user.get() is None

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="user", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


# These endpoints are relatively simple, just check response and args
@pytest.mark.parametrize(
    ("method_name", "http_method", "endpoint"),
    [
        ("get_me", "GET", "user/me"),
        ("unread_count", "GET", "user/unread_count"),
        ("mark_all_as_read", "POST", "user/mark_all_as_read"),
        ("notifications_count", "GET", "user/notifications_count"),
        ("mark_all_notifications_read", "PUT", "user/mark_all_notifications_read"),
        ("get_captcha", "GET", "user/get_captcha"),
    ],
)
def test_simple_endpoints(method_name: str, http_method: str, endpoint: str):
    async def run_test():
        response = {"result": "ok"}
        user, client = make_user(response)

        # Check response
        assert await getattr(user, method_name)() == response

        # Check args
        client.request.assert_awaited_once_with(method=http_method, endpoint=endpoint)

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_login():
    async def run_test():
        response = {"jwt": "token"}
        user, client = make_user(response)

        # login method of User class should return a dict
        assert await user.login(username_or_email="test_user", password="hunter2") == response

        # Check args
        client.log_in.assert_awaited_once_with(
            username_or_email="test_user",
            password="hunter2",
            return_dict=True,
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_logout():
    async def run_test():
        response = {"logged_out": True}
        user, client = make_user(response)

        # logout method of User class should return a dict
        assert await user.logout() == response

        # Check args
        client.log_out.assert_awaited_once_with(return_dict=True)

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_block_domain():
    async def run_test():
        response = {"blocked": False}
        user, client = make_user(response)

        # Check response
        assert await user.block_domain(domain="example.org", block=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="domain/block",
            data={"block": False, "domain": "example.org"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_user_block():
    async def run_test():
        response = {"blocked": False}
        user, client = make_user(response)

        # Check response
        assert await user.user_block(person_id=42, block=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/block",
            data={"block": False, "person_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_user_subscribe():
    async def run_test():
        response = {"subscribed": False}
        user, client = make_user(response)

        # Check response
        assert await user.user_subscribe(person_id=42, subscribe=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="user/subscribe",
            data={"person_id": 42, "subscribe": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_mark_notification_as_read():
    async def run_test():
        response = {"notif_id": 42}
        user, client = make_user(response)

        # Check response
        assert await user.mark_notification_as_read(notif_id=42, read_state=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="user/notification_state",
            data={"notif_id": 42, "read_state": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_verify_credentials():
    async def run_test():
        response = True
        user, client = make_user(response)

        # Good response for this endpoint is just 200 with no body, so request just returns True
        assert await user.verify_credentials(username="test_user", password="hunter2") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/verify_credentials",
            data={"username": "test_user", "password": "hunter2"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_set_flair():
    async def run_test():
        response = {"activity_alert": False}
        user, client = make_user(response)

        # Check response
        assert await user.set_flair(community_id=3, flair_text="noob") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/set_flair",
            data={"community_id": 3, "flair_text": "noob"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_follow_user():
    async def run_test():
        response = {"ok": "ok"}
        user, client = make_user(response)

        # Check response
        assert await user.follow_user(user_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/follow",
            data={"user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_unfollow_user():
    async def run_test():
        response = {"ok": "ok"}
        user, client = make_user(response)

        # Check response
        assert await user.unfollow_user(user_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/unfollow",
            data={"user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_user_note():
    async def run_test():
        response = {"person_view": {"activity_alert": True}}
        user, client = make_user(response)

        # Check response
        assert await user.user_note(person_id=42, note="obv bot") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/note",
            data={"person_id": 42, "note": "obv bot"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_unban_user():
    async def run_test():
        response = {"person_view": {"activity_alert": True}}
        user, client = make_user(response)

        # Check response
        assert await user.unban_user(person_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/unban",
            data={"person_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_ban_user():
    async def run_test():
        response = {"person_view": {"activity_alert": True}}
        user, client = make_user(response)

        # Check response
        assert await user.ban_user(42, ban_ip_address=True, purge_content=False, reason="spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/ban",
            data={
                "person_id": 42,
                "ban_ip_address": True,
                "purge_content": False,
                "reason": "spam",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


# These endpoints all basically look the same and have the same args
@pytest.mark.parametrize("method_name", ["replies", "mentions", "media"])
def test_feed_endpoints(method_name: str):
    async def run_test():
        response = {"next_page": "2"}
        user, client = make_user(response)

        # Check response
        assert await getattr(user, method_name)(limit=20, page=2, sort="New", unread_only=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint=f"user/{method_name}",
            params={"limit": 20, "page": 2, "sort": "New", "unread_only": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


# Test these endpoints when None is returned by request
@pytest.mark.parametrize("method_name", ["replies", "mentions", "media"])
def test_feed_endpoint_raising(method_name: str):
    async def run_test():
        user, client = make_user(None, raise_exceptions=False)

        # Should return None when None is returned by the request
        assert await getattr(user, method_name)() is None

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint=f"user/{method_name}", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


# Lots of different possible args in this endpoint
def test_save_user_settings():
    async def run_test():
        response = {"my_user": "lots of other stuff here"}
        user, client = make_user(response)
        extra_fields = [{"id": 1, "label": "Pronouns", "text": "they/them"}]
        settings = {
            "accept_private_messages": "All",
            "avatar": "https://site.tld/avatar.png",
            "bio": "Hello",
            "bot": False,
            "bot_visibility": "Show",
            "reposter_visibility": "Show",
            "community_keyword_filter": ["dorito"],
            "cover": "https://site.tld/cover.png",
            "default_comment_sort_type": "Old",
            "default_sort_type": "New",
            "display_name": "Test User",
            "email_unread": False,
            "extra_fields": extra_fields,
            "federate_votes": False,
            "feed_auto_follow": True,
            "feed_auto_leave": False,
            "hide_low_quality": True,
            "indexable": False,
            "newsletter": True,
            "nsfl_visibility": "Show",
            "nsfw_visibility": "Hide",
            "genai_visibility": "Transparent",
            "reply_collapse_threshold": -5,
            "reply_hide_threshold": -10,
            "show_nsfw": False,
            "show_nsfl": True,
            "show_read_posts": False,
            "searchable": True,
            "matrix_user_id": "@test:example.org",
        }

        # Check response
        assert await user.save_user_settings(**settings) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="user/save_user_settings",
            data=settings,
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_save_user_settings_raising():
    async def run_test():
        user, client = make_user(None, raise_exceptions=False)

        # Return None when None returned by request
        assert await user.save_user_settings(searchable=True) is None

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="user/save_user_settings",
            data={"searchable": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


# Test that passing an empty string to certain fields will include them in the data dict as None
def test_save_user_settings_nullable():
    async def run_test():
        response = {"my_user": "lots of other stuff here"}
        user, client = make_user(response)

        settings = {
            "avatar": "",
            "bio": "",
            "community_keyword_filter": "",
            "cover": "",
            "display_name": "",
            "matrix_user_id": "",
        }

        # Check response
        assert await user.save_user_settings(**settings) == response

        # Check args, should be None after passing in an empty string
        correct_data = {
            "avatar": None,
            "bio": None,
            "community_keyword_filter": None,
            "cover": None,
            "display_name": None,
            "matrix_user_id": None,
        }

        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="user/save_user_settings",
            data=correct_data,
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_notifications():
    async def run_test():
        response = {"next_page": "2"}
        user, client = make_user(response)

        # Check response
        assert await user.get_notifications(status="unread", limit="20", page=2) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="user/notifications",
            params={"status": "unread", "limit": "20", "page": 2},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_notifications_raising():
    async def run_test():
        user, client = make_user(None, raise_exceptions=False)

        # Check response
        assert await user.get_notifications() is None

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="user/notifications", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_activity_alerts():
    async def run_test():
        response = {"next_page": "2"}
        user, client = make_user(response)

        # Check response
        assert await user.list_activity_alerts(type_="Posts", filter="All", sort="New", page=2, limit=20) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="user/activity_alert/list",
            params={"type_": "Posts", "filter": "All", "sort": "New", "page": 2, "limit": 20},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_activity_alert_create():
    async def run_test():
        response = {"activity_alert": True}
        user, client = make_user(response)
        alert = {
            "post_id": 1,
            "comment_id": 2,
            "person_id": 3,
            "topic_id": 4,
            "feed_id": 5,
            "community_id": 6,
        }

        # Check response
        assert await user.activity_alert_create(**alert) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/activity_alert",
            data=alert,
        )

    asyncio.run(run_test())


def test_activity_alert_delete():
    async def run_test():
        response = {"activity_alert": False}
        user, client = make_user(response)
        alert = {
            "post_id": 1,
            "comment_id": 2,
            "person_id": 3,
            "topic_id": 4,
            "feed_id": 5,
            "community_id": 6,
        }

        # Check response
        assert await user.activity_alert_delete(**alert) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="user/activity_alert/delete",
            data=alert,
        )

    asyncio.run(run_test())


def test_register():
    async def run_test():
        user, _ = make_user({})

        # This endpoint is unimplemented, just raise an error
        with pytest.raises(NotImplementedError):
            await user.register()

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_register_raising():
    async def run_test():
        user, client = make_user(None, raise_exceptions=False)

        # Exception should be ignored with set to not raise
        assert await user.register() is None
        assert client.raise_exceptions is False

    # Start the event loop and run the test
    asyncio.run(run_test())
