import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from pieforhead.exceptions import NotImplementedError
from pieforhead.post import PostAsync


def make_post(response: dict | bool | None, raise_exceptions: bool = True) -> tuple[PostAsync, Mock]:
    """Make a mock PostAsync class to return toy data."""
    client = Mock()
    client.request = AsyncMock(return_value=response)
    client.raise_exceptions = raise_exceptions

    return PostAsync(client), client


def test_list_posts_all_params():
    async def run_test():
        response = {"posts": []}
        post, client = make_post(response)

        # Check response
        assert (
            await post.list_posts(
                query="python",
                sort="New",
                type_="Local",
                community_name="python",
                community_id=42,
                saved_only=False,
                nsfw="Exclude",
                person_id=84,
                limit=20,
                page=2,
                liked_only=True,
                feed_id=10,
                topic_id=11,
                ignore_sticky=True,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="post/list",
            params={
                "q": "python",
                "sort": "New",
                "type_": "Local",
                "community_name": "python",
                "community_id": 42,
                "saved_only": False,
                "nsfw": "Exclude",
                "person_id": 84,
                "limit": 20,
                "page": 2,
                "liked_only": True,
                "feed_id": 10,
                "topic_id": 11,
                "ignore_sticky": True,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_posts_defaults():
    async def run_test():
        response = {"posts": []}
        post, client = make_post(response)

        # Check response
        assert await post.list_posts() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="post/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_posts_2_unimplemented():
    async def run_test():
        post, client = make_post({})

        # Check that the unimplemented endpoint raises
        with pytest.raises(NotImplementedError):
            await post.list_posts_2()

        # Check that no request is sent
        client.request.assert_not_awaited()

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_posts_2_unimplemented_suppressed():
    async def run_test():
        post, client = make_post(None, raise_exceptions=False)

        # Check that errors are suppressed
        assert await post.list_posts_2() is None

        # Check that no request is sent
        client.request.assert_not_awaited()

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_scheduled_all_params():
    async def run_test():
        response = {"scheduled_posts": []}
        post, client = make_post(response)

        # Check response
        assert (
            await post.list_scheduled(
                query="draft",
                sort="Old",
                community_name="python",
                community_id=42,
                include_deleted=False,
                limit=20,
                page=2,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="post/scheduled/list",
            params={
                "q": "draft",
                "sort": "Old",
                "community_name": "python",
                "community_id": 42,
                "include_deleted": False,
                "limit": 20,
                "page": 2,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_scheduled_defaults():
    async def run_test():
        response = {"scheduled_posts": []}
        post, client = make_post(response)

        # Check response
        assert await post.list_scheduled() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="post/scheduled/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.get(post_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="post", params={"id": 42})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_all_params():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Some toy event and poll structures
        event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
        poll = {"mode": "single", "choices": []}

        # Check response
        assert (
            await post.create(
                title="Python",
                community_id=42,
                alt_text="Description",
                body="Post body",
                url="https://site.tld",
                og_image_url="https://site.tld/image.png",
                nsfw=False,
                ai_generated=True,
                language_id=1,
                event=event,
                poll=poll,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post",
            data={
                "title": "Python",
                "community_id": 42,
                "alt_text": "Description",
                "body": "Post body",
                "url": "https://site.tld",
                "og_image_url": "https://site.tld/image.png",
                "nsfw": False,
                "ai_generated": True,
                "language_id": 1,
                "event": event,
                "poll": poll,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_defaults():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.create(title="Python", community_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post",
            data={"title": "Python", "community_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_all_params():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Some toy event and poll structures
        event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
        poll = {"mode": "single", "choices": []}

        # Check response
        assert (
            await post.edit(
                post_id=42,
                alt_text="Description",
                title="Updated",
                body="Updated body",
                url="https://site.tld",
                nsfw=False,
                language_id=1,
                event=event,
                poll=poll,
                tags="python,api",
                flair="Question",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="post",
            data={
                "post_id": 42,
                "title": "Updated",
                "body": "Updated body",
                "nsfw": False,
                "language_id": 1,
                "event": event,
                "poll": poll,
                "alt_text": "Description",
                "url": "https://site.tld",
                "tags": "python,api",
                "flair": "Question",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_nullable_fields():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.edit(post_id=42, alt_text="", url="", tags="", flair="") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="post",
            data={"post_id": 42, "alt_text": None, "url": None, "tags": None, "flair": None},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_scheduled():
    async def run_test():
        response = {"scheduled_post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.get_scheduled(post_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="post/scheduled", params={"id": 42})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_scheduled_all_params():
    async def run_test():
        response = {"scheduled_post_view": {}}
        post, client = make_post(response)

        # Some toy event and poll structures
        event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
        poll = {"mode": "single", "choices": []}

        # Check response
        assert (
            await post.create_scheduled(
                title="Scheduled",
                community_id=42,
                scheduled_for="2027-01-01T00:00:00Z",
                alt_text="Description",
                body="Post body",
                url="https://site.tld",
                og_image_url="https://site.tld/image.png",
                nsfw=False,
                ai_generated=True,
                language_id=1,
                event=event,
                poll=poll,
                repeat="Weekly",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/scheduled",
            data={
                "title": "Scheduled",
                "community_id": 42,
                "scheduled_for": "2027-01-01T00:00:00Z",
                "alt_text": "Description",
                "body": "Post body",
                "url": "https://site.tld",
                "og_image_url": "https://site.tld/image.png",
                "nsfw": False,
                "ai_generated": True,
                "language_id": 1,
                "event": event,
                "poll": poll,
                "repeat": "Weekly",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_scheduled_defaults():
    async def run_test():
        response = {"scheduled_post_view": {}}
        post, client = make_post(response)

        # Check response
        assert (
            await post.create_scheduled(
                title="Scheduled",
                community_id=42,
                scheduled_for="2027-01-01T00:00:00Z",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/scheduled",
            data={"title": "Scheduled", "community_id": 42, "scheduled_for": "2027-01-01T00:00:00Z"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_scheduled_all_params():
    async def run_test():
        response = {"scheduled_post_view": {}}
        post, client = make_post(response)

        # Some toy event and poll structures
        event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
        poll = {"mode": "single", "choices": []}

        # Check response
        assert (
            await post.edit_scheduled(
                post_id=42,
                alt_text="Description",
                title="Updated",
                body="Updated body",
                url="https://site.tld",
                nsfw=False,
                language_id=1,
                event=event,
                poll=poll,
                tags="python,api",
                flair="Question",
                scheduled_for="2027-01-02T00:00:00Z",
                repeat="Monthly",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="post/scheduled",
            data={
                "post_id": 42,
                "title": "Updated",
                "body": "Updated body",
                "nsfw": False,
                "language_id": 1,
                "event": event,
                "poll": poll,
                "scheduled_for": "2027-01-02T00:00:00Z",
                "repeat": "Monthly",
                "alt_text": "Description",
                "url": "https://site.tld",
                "tags": "python,api",
                "flair": "Question",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_scheduled_nullable_fields():
    async def run_test():
        response = {"scheduled_post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.edit_scheduled(post_id=42, alt_text="", url="", tags="", flair="") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="post/scheduled",
            data={"post_id": 42, "alt_text": None, "url": None, "tags": None, "flair": None},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_replies_all_params():
    async def run_test():
        response = {"comments": []}
        post, client = make_post(response)

        # Check response
        assert await post.replies(post_id=42, parent_id=84, sort="Top", max_depth=3, page="2", limit=20) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="post/replies",
            params={"post_id": 42, "parent_id": 84, "sort": "Top", "max_depth": 3, "page": "2", "limit": 20},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_replies_defaults():
    async def run_test():
        response = {"comments": []}
        post, client = make_post(response)

        # Check response
        assert await post.replies() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="post/replies", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_site_metadata():
    async def run_test():
        response = {"metadata": {}}
        post, client = make_post(response)

        # Check response
        assert await post.site_metadata(url="https://site.tld") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="post/site_metadata",
            params={"url": "https://site.tld"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_like_all_params():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.like(post_id=42, score=1, private=False, emoji="✅") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/like",
            data={"post_id": 42, "score": 1, "private": False, "emoji": "✅"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_like_defaults():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.like(post_id=42, score=0) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/like",
            data={"post_id": 42, "score": 0},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_save():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.save(post_id=42, save=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="post/save",
            data={"post_id": 42, "save": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_subscribe():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.subscribe(post_id=42, subscribe=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="post/subscribe",
            data={"post_id": 42, "subscribe": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.delete(post_id=42, deleted=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/delete",
            data={"post_id": 42, "deleted": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete_scheduled():
    async def run_test():
        response = {"scheduled_post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.delete_scheduled(post_id=42, deleted=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/scheduled/delete",
            data={"post_id": 42, "deleted": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_report_all_params():
    async def run_test():
        response = {"post_report_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.report(post_id=42, reason="Spam", description="Details", report_remote=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/report",
            data={"post_id": 42, "reason": "Spam", "description": "Details", "report_remote": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_report_defaults():
    async def run_test():
        response = {"post_report_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.report(post_id=42, reason="Spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/report",
            data={"post_id": 42, "reason": "Spam"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_reports_all_params():
    async def run_test():
        response = {"post_reports": []}
        post, client = make_post(response)

        # Check response
        assert (
            await post.list_reports(community_id=42, limit=10, page=2, post_id=84, unresolved_only=False) == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="post/report/list",
            params={"community_id": 42, "limit": 10, "page": 2, "post_id": 84, "unresolved_only": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_reports_defaults():
    async def run_test():
        response = {"post_reports": []}
        post, client = make_post(response)

        # Check response
        assert await post.list_reports() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="post/report/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_resolve_report():
    async def run_test():
        response = {"post_report_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.resolve_report(report_id=42, resolved=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="post/report/resolve",
            data={"report_id": 42, "resolved": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_lock():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.lock(post_id=42, locked=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/lock",
            data={"post_id": 42, "locked": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_hide():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.hide(post_id=42, hidden=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/hide",
            data={"post_id": 42, "hidden": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_feature_all_params():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.feature(post_id=42, featured=True, feature_type="Community") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/feature",
            data={"post_id": 42, "featured": True, "feature_type": "Community"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_feature_defaults():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.feature(post_id=42, featured=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/feature",
            data={"post_id": 42, "featured": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_remove_all_params():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.remove(post_id=42, removed=True, reason="Spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/remove",
            data={"post_id": 42, "removed": True, "reason": "Spam"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_remove_defaults():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.remove(post_id=42, removed=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/remove",
            data={"post_id": 42, "removed": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_mark_as_read_single_post():
    async def run_test():
        response = {"success": True}
        post, client = make_post(response)

        # Check response
        assert await post.mark_as_read(read=True, post_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/mark_as_read",
            data={"read": True, "post_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_mark_as_read_multiple_posts():
    async def run_test():
        response = {"success": True}
        post, client = make_post(response)

        # Check response
        assert await post.mark_as_read(read=False, post_ids=[42, 84]) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/mark_as_read",
            data={"read": False, "post_ids": [42, 84]},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_likes_all_params():
    async def run_test():
        response = {"post_likes": []}
        post, client = make_post(response)

        # Check response
        assert await post.list_likes(post_id=42, page=2, limit=10) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="post/like/list",
            params={"post_id": 42, "page": 2, "limit": 10},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_likes_defaults():
    async def run_test():
        response = {"post_likes": []}
        post, client = make_post(response)

        # Check response
        assert await post.list_likes(post_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="post/like/list",
            params={"post_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_assign_flair():
    async def run_test():
        response = {"post": {}}
        post, client = make_post(response)

        # Check response
        assert await post.assign_flair(post_id=42, flair_id_list=[1, 2]) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/assign_flair",
            data={"post_id": 42, "flair_id_list": [1, 2]},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_assign_flair_nullable_fields():
    async def run_test():
        response = {"post": {}}
        post, client = make_post(response)

        # Check response
        assert await post.assign_flair(post_id=42, flair_id_list=[]) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/assign_flair",
            data={"post_id": 42, "flair_id_list": None},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_poll_vote():
    async def run_test():
        response = {"post_view": {}}
        post, client = make_post(response)

        # Check response
        assert await post.poll_vote(post_id=42, choice_id=[1, 2]) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="post/poll_vote",
            data={"post_id": 42, "choice_id": [1, 2]},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())
