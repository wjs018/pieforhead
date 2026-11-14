from unittest.mock import Mock

from pieforhead.comment import Comment


def make_comment(response: dict | bool | None) -> tuple[Comment, Mock]:
    """Make a mock Comment class to return toy data."""
    client = Mock()
    client.request.return_value = response

    return Comment(client), client


def test_list_comments_all_params():
    response = {"comments": []}
    comment, client = make_comment(response)

    # Check response
    assert (
        comment.list_comments(
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
    client.request.assert_called_once_with(
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


def test_list_comments_defaults():
    response = {"comments": []}
    comment, client = make_comment(response)

    # Check response
    assert comment.list_comments() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="comment/list", params={})


def test_get():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.get(comment_id=42) == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="comment", params={"id": 42})


def test_create_all_params():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.create(body="A reply", post_id=42, parent_id=84, language_id=1) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment",
        data={"body": "A reply", "post_id": 42, "parent_id": 84, "language_id": 1},
    )


def test_create_defaults():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.create(body="A comment", post_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment",
        data={"body": "A comment", "post_id": 42},
    )


def test_edit_all_params():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.edit(comment_id=42, body="Edited reply", language_id=1, distinguished=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="comment",
        data={"comment_id": 42, "body": "Edited reply", "language_id": 1, "distinguished": False},
    )


def test_edit_defaults():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.edit(comment_id=42, body="Edited reply") == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="comment",
        data={"comment_id": 42, "body": "Edited reply"},
    )


def test_like_all_params():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.like(comment_id=42, score=1, private=False, emoji="✅") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/like",
        data={"comment_id": 42, "score": 1, "private": False, "emoji": "✅"},
    )


def test_like_defaults():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.like(comment_id=42, score=-1) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/like",
        data={"comment_id": 42, "score": -1},
    )


def test_save():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.save(comment_id=42, save=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="comment/save",
        data={"comment_id": 42, "save": True},
    )


def test_subscribe():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.subscribe(comment_id=42, subscribe=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="comment/subscribe",
        data={"comment_id": 42, "subscribe": False},
    )


def test_delete():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.delete(comment_id=42, deleted=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/delete",
        data={"comment_id": 42, "deleted": True},
    )


def test_report_all_params():
    response = {"comment_report_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.report(comment_id=42, reason="Spam", description="Details", report_remote=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/report",
        data={"comment_id": 42, "reason": "Spam", "description": "Details", "report_remote": False},
    )


def test_report_defaults():
    response = {"comment_report_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.report(comment_id=42, reason="Spam") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/report",
        data={"comment_id": 42, "reason": "Spam"},
    )


def test_list_reports_all_params():
    response = {"comment_reports": []}
    comment, client = make_comment(response)

    # Check response
    assert comment.list_reports(comment_id=42, community_id=84, limit=20, page=2, unresolved_only=False) == response

    # Check args
    client.request.assert_called_once_with(
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


def test_list_reports_defaults():
    response = {"comment_reports": []}
    comment, client = make_comment(response)

    # Check response
    assert comment.list_reports() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="comment/report/list", params={})


def test_resolve_report():
    response = {"comment_report_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.resolve_report(report_id=42, resolved=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="comment/report/resolve",
        data={"report_id": 42, "resolved": True},
    )


def test_remove_all_params():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.remove(comment_id=42, removed=True, reason="Spam") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/remove",
        data={"comment_id": 42, "removed": True, "reason": "Spam"},
    )


def test_remove_defaults():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.remove(comment_id=42, removed=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/remove",
        data={"comment_id": 42, "removed": False},
    )


def test_mark_as_read():
    response = {"comment_reply_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.mark_as_read(comment_reply_id=42, read=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/mark_as_read",
        data={"comment_reply_id": 42, "read": True},
    )


def test_mark_as_answer():
    response = {"comment_reply_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.mark_as_answer(comment_reply_id=42, answer=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/mark_as_answer",
        data={"comment_reply_id": 42, "answer": True},
    )


def test_distinguish():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.distinguish(comment_reply_id=42, distinguished=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/distinguish",
        data={"comment_reply_id": 42, "distinguished": True},
    )


def test_lock():
    response = {"comment_view": {}}
    comment, client = make_comment(response)

    # Check response
    assert comment.lock(comment_id=42, locked=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="comment/lock",
        data={"comment_id": 42, "locked": True},
    )


def test_list_likes_all_params():
    response = {"comment_likes": []}
    comment, client = make_comment(response)

    # Check response
    assert comment.list_likes(comment_id=42, page=2, limit=20) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="comment/like/list",
        params={"comment_id": 42, "page": 2, "limit": 20},
    )


def test_list_likes_defaults():
    response = {"comment_likes": []}
    comment, client = make_comment(response)

    # Check response
    assert comment.list_likes(comment_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="comment/like/list",
        params={"comment_id": 42},
    )
