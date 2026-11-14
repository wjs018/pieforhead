import asyncio
from unittest.mock import AsyncMock, Mock

from pieforhead.comment import CommentAsync


def make_comment(response: dict | bool | None) -> tuple[CommentAsync, Mock]:
    """Make a mock CommentAsync class to return toy data."""
    client = Mock()
    client.request = AsyncMock(return_value=response)

    return CommentAsync(client), client


def test_list_comments_all_params():
    async def run_test():
        response = {"comments": []}
        comment, client = make_comment(response)

        # Check response
        assert (
            await comment.list_comments(
                limit=20,
                page=2,
                sort="New",
                type_="Local",
                liked_only=False,
                saved_only=True,
                person_id=84,
                community_id=42,
                post_id=13,
                parent_id=14,
                max_depth=3,
                depth_first=False,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="comment/list",
            params={
                "limit": 20,
                "page": 2,
                "sort": "New",
                "type_": "Local",
                "liked_only": False,
                "saved_only": True,
                "person_id": 84,
                "community_id": 42,
                "post_id": 13,
                "parent_id": 14,
                "max_depth": 3,
                "depth_first": False,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_comments_defaults():
    async def run_test():
        response = {"comments": []}
        comment, client = make_comment(response)

        # Check response
        assert await comment.list_comments() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="comment/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.get(comment_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="comment", params={"id": 42})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_all_params():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.create(body="A reply", post_id=42, parent_id=84, language_id=1) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment",
            data={"body": "A reply", "post_id": 42, "parent_id": 84, "language_id": 1},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_defaults():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.create(body="A comment", post_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment",
            data={"body": "A comment", "post_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_all_params():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.edit(comment_id=42, body="Edited reply", language_id=1, distinguished=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="comment",
            data={"comment_id": 42, "body": "Edited reply", "language_id": 1, "distinguished": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_defaults():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.edit(comment_id=42, body="Edited reply") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="comment",
            data={"comment_id": 42, "body": "Edited reply"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_like_all_params():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.like(comment_id=42, score=1, private=False, emoji="✅") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/like",
            data={"comment_id": 42, "score": 1, "private": False, "emoji": "✅"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_like_defaults():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.like(comment_id=42, score=-1) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/like",
            data={"comment_id": 42, "score": -1},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_save():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.save(comment_id=42, save=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="comment/save",
            data={"comment_id": 42, "save": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_subscribe():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.subscribe(comment_id=42, subscribe=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="comment/subscribe",
            data={"comment_id": 42, "subscribe": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.delete(comment_id=42, deleted=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/delete",
            data={"comment_id": 42, "deleted": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_report_all_params():
    async def run_test():
        response = {"comment_report_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.report(comment_id=42, reason="Spam", description="Details", report_remote=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/report",
            data={"comment_id": 42, "reason": "Spam", "description": "Details", "report_remote": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_report_defaults():
    async def run_test():
        response = {"comment_report_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.report(comment_id=42, reason="Spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/report",
            data={"comment_id": 42, "reason": "Spam"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_reports_all_params():
    async def run_test():
        response = {"comment_reports": []}
        comment, client = make_comment(response)

        # Check response
        assert (
            await comment.list_reports(comment_id=42, community_id=84, limit=20, page=2, unresolved_only=False)
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="comment/report/list",
            params={
                "comment_id": 42,
                "community_id": 84,
                "limit": 20,
                "page": 2,
                "unresolved_only": False,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_reports_defaults():
    async def run_test():
        response = {"comment_reports": []}
        comment, client = make_comment(response)

        # Check response
        assert await comment.list_reports() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="comment/report/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_resolve_report():
    async def run_test():
        response = {"comment_report_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.resolve_report(report_id=42, resolved=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="comment/report/resolve",
            data={"report_id": 42, "resolved": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_remove_all_params():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.remove(comment_id=42, removed=True, reason="Spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/remove",
            data={"comment_id": 42, "removed": True, "reason": "Spam"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_remove_defaults():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.remove(comment_id=42, removed=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/remove",
            data={"comment_id": 42, "removed": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_mark_as_read():
    async def run_test():
        response = {"comment_reply_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.mark_as_read(comment_reply_id=42, read=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/mark_as_read",
            data={"comment_reply_id": 42, "read": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_mark_as_answer():
    async def run_test():
        response = {"comment_reply_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.mark_as_answer(comment_reply_id=42, answer=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/mark_as_answer",
            data={"comment_reply_id": 42, "answer": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_distinguish():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.distinguish(comment_reply_id=42, distinguished=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/distinguish",
            data={"comment_reply_id": 42, "distinguished": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_lock():
    async def run_test():
        response = {"comment_view": {}}
        comment, client = make_comment(response)

        # Check response
        assert await comment.lock(comment_id=42, locked=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="comment/lock",
            data={"comment_id": 42, "locked": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_likes_all_params():
    async def run_test():
        response = {"comment_likes": []}
        comment, client = make_comment(response)

        # Check response
        assert await comment.list_likes(comment_id=42, page=2, limit=20) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="comment/like/list",
            params={"comment_id": 42, "page": 2, "limit": 20},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_likes_defaults():
    async def run_test():
        response = {"comment_likes": []}
        comment, client = make_comment(response)

        # Check response
        assert await comment.list_likes(comment_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="comment/like/list",
            params={"comment_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())