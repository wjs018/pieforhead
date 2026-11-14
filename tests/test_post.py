from unittest.mock import Mock

import pytest

from pieforhead.exceptions import NotImplementedError
from pieforhead.post import Post


def make_post(response: dict | bool | None, raise_exceptions: bool = True) -> tuple[Post, Mock]:
    """Make a mock Post class to return toy data."""
    client = Mock()
    client.request.return_value = response
    client.raise_exceptions = raise_exceptions

    return Post(client), client


def test_list_posts_all_params():
    response = {"posts": []}
    post, client = make_post(response)

    # Check response
    assert (
        post.list_posts(
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
    client.request.assert_called_once_with(
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


def test_list_posts_defaults():
    response = {"posts": []}
    post, client = make_post(response)

    # Check response
    assert post.list_posts() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="post/list", params={})


def test_list_posts_2_unimplemented():
    post, client = make_post({})

    # Check that the unimplemented endpoint raises
    with pytest.raises(NotImplementedError):
        post.list_posts_2()

    # Check that no request is sent
    client.request.assert_not_called()


def test_list_posts_2_unimplemented_suppressed():
    post, client = make_post(None, raise_exceptions=False)

    # Check that errors are suppressed
    assert post.list_posts_2() is None

    # Check that no request is sent
    client.request.assert_not_called()


def test_list_scheduled_all_params():
    response = {"scheduled_posts": []}
    post, client = make_post(response)

    # Check response
    assert (
        post.list_scheduled(
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
    client.request.assert_called_once_with(
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


def test_list_scheduled_defaults():
    response = {"scheduled_posts": []}
    post, client = make_post(response)

    # Check response
    assert post.list_scheduled() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="post/scheduled/list", params={})


def test_get():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.get(post_id=42) == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="post", params={"id": 42})


def test_create_all_params():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Some toy event and poll structures
    event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
    poll = {"mode": "single", "choices": []}

    # Check response
    assert (
        post.create(
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
    client.request.assert_called_once_with(
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


def test_create_defaults():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.create(title="Python", community_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post",
        data={"title": "Python", "community_id": 42},
    )


def test_edit_all_params():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Some toy event and poll structures
    event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
    poll = {"mode": "single", "choices": []}

    # Check response
    assert (
        post.edit(
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
    client.request.assert_called_once_with(
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


def test_edit_nullable_fields():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.edit(post_id=42, alt_text="", url="", tags="", flair="") == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="post",
        data={"post_id": 42, "alt_text": None, "url": None, "tags": None, "flair": None},
    )


def test_get_scheduled():
    response = {"scheduled_post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.get_scheduled(post_id=42) == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="post/scheduled", params={"id": 42})


def test_create_scheduled_all_params():
    response = {"scheduled_post_view": {}}
    post, client = make_post(response)

    # Some toy event and poll structures
    event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
    poll = {"mode": "single", "choices": []}

    # Check response
    assert (
        post.create_scheduled(
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
    client.request.assert_called_once_with(
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


def test_create_scheduled_defaults():
    response = {"scheduled_post_view": {}}
    post, client = make_post(response)

    # Check response
    assert (
        post.create_scheduled(
            title="Scheduled",
            community_id=42,
            scheduled_for="2027-01-01T00:00:00Z",
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/scheduled",
        data={"title": "Scheduled", "community_id": 42, "scheduled_for": "2027-01-01T00:00:00Z"},
    )


def test_edit_scheduled_all_params():
    response = {"scheduled_post_view": {}}
    post, client = make_post(response)

    # Some toy event and poll structures
    event = {"start": "2027-01-01T00:00:00Z", "end": "2027-01-02T00:00:00Z"}
    poll = {"mode": "single", "choices": []}

    # Check response
    assert (
        post.edit_scheduled(
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
    client.request.assert_called_once_with(
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


def test_edit_scheduled_nullable_fields():
    response = {"scheduled_post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.edit_scheduled(post_id=42, alt_text="", url="", tags="", flair="") == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="post/scheduled",
        data={"post_id": 42, "alt_text": None, "url": None, "tags": None, "flair": None},
    )


def test_replies_all_params():
    response = {"comments": []}
    post, client = make_post(response)

    # Check response
    assert post.replies(post_id=42, parent_id=84, sort="Top", max_depth=3, page="2", limit=20) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="post/replies",
        params={"post_id": 42, "parent_id": 84, "sort": "Top", "max_depth": 3, "page": "2", "limit": 20},
    )


def test_replies_defaults():
    response = {"comments": []}
    post, client = make_post(response)

    # Check response
    assert post.replies() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="post/replies", params={})


def test_site_metadata():
    response = {"metadata": {}}
    post, client = make_post(response)

    # Check response
    assert post.site_metadata(url="https://site.tld") == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="post/site_metadata",
        params={"url": "https://site.tld"},
    )


def test_like_all_params():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.like(post_id=42, score=1, private=False, emoji="✅") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/like",
        data={"post_id": 42, "score": 1, "private": False, "emoji": "✅"},
    )


def test_like_defaults():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.like(post_id=42, score=0) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/like",
        data={"post_id": 42, "score": 0},
    )


def test_save():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.save(post_id=42, save=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="post/save",
        data={"post_id": 42, "save": False},
    )


def test_subscribe():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.subscribe(post_id=42, subscribe=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="post/subscribe",
        data={"post_id": 42, "subscribe": True},
    )


def test_delete():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.delete(post_id=42, deleted=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/delete",
        data={"post_id": 42, "deleted": True},
    )


def test_delete_scheduled():
    response = {"scheduled_post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.delete_scheduled(post_id=42, deleted=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/scheduled/delete",
        data={"post_id": 42, "deleted": True},
    )


def test_report_all_params():
    response = {"post_report_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.report(post_id=42, reason="Spam", description="Details", report_remote=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/report",
        data={"post_id": 42, "reason": "Spam", "description": "Details", "report_remote": False},
    )


def test_report_defaults():
    response = {"post_report_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.report(post_id=42, reason="Spam") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/report",
        data={"post_id": 42, "reason": "Spam"},
    )


def test_list_reports_all_params():
    response = {"post_reports": []}
    post, client = make_post(response)

    # Check response
    assert post.list_reports(community_id=42, limit=10, page=2, post_id=84, unresolved_only=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="post/report/list",
        params={"community_id": 42, "limit": 10, "page": 2, "post_id": 84, "unresolved_only": False},
    )


def test_list_reports_defaults():
    response = {"post_reports": []}
    post, client = make_post(response)

    # Check response
    assert post.list_reports() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="post/report/list", params={})


def test_resolve_report():
    response = {"post_report_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.resolve_report(report_id=42, resolved=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="post/report/resolve",
        data={"report_id": 42, "resolved": True},
    )


def test_lock():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.lock(post_id=42, locked=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/lock",
        data={"post_id": 42, "locked": True},
    )


def test_hide():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.hide(post_id=42, hidden=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/hide",
        data={"post_id": 42, "hidden": True},
    )


def test_feature_all_params():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.feature(post_id=42, featured=True, feature_type="Community") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/feature",
        data={"post_id": 42, "featured": True, "feature_type": "Community"},
    )


def test_feature_defaults():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.feature(post_id=42, featured=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/feature",
        data={"post_id": 42, "featured": False},
    )


def test_remove_all_params():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.remove(post_id=42, removed=True, reason="Spam") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/remove",
        data={"post_id": 42, "removed": True, "reason": "Spam"},
    )


def test_remove_defaults():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.remove(post_id=42, removed=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/remove",
        data={"post_id": 42, "removed": False},
    )


def test_mark_as_read_single_post():
    response = {"success": True}
    post, client = make_post(response)

    # Check response
    assert post.mark_as_read(read=True, post_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/mark_as_read",
        data={"read": True, "post_id": 42},
    )


def test_mark_as_read_multiple_posts():
    response = {"success": True}
    post, client = make_post(response)

    # Check response
    assert post.mark_as_read(read=False, post_ids=[42, 84]) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/mark_as_read",
        data={"read": False, "post_ids": [42, 84]},
    )


def test_list_likes_all_params():
    response = {"post_likes": []}
    post, client = make_post(response)

    # Check response
    assert post.list_likes(post_id=42, page=2, limit=10) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="post/like/list",
        params={"post_id": 42, "page": 2, "limit": 10},
    )


def test_list_likes_defaults():
    response = {"post_likes": []}
    post, client = make_post(response)

    # Check response
    assert post.list_likes(post_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="post/like/list",
        params={"post_id": 42},
    )


def test_assign_flair():
    response = {"post": {}}
    post, client = make_post(response)

    # Check response
    assert post.assign_flair(post_id=42, flair_id_list=[1, 2]) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/assign_flair",
        data={"post_id": 42, "flair_id_list": [1, 2]},
    )


def test_assign_flair_nullable_fields():
    response = {"post": {}}
    post, client = make_post(response)

    # Check response
    assert post.assign_flair(post_id=42, flair_id_list=[]) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/assign_flair",
        data={"post_id": 42, "flair_id_list": None},
    )


def test_poll_vote():
    response = {"post_view": {}}
    post, client = make_post(response)

    # Check response
    assert post.poll_vote(post_id=42, choice_id=[1, 2]) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="post/poll_vote",
        data={"post_id": 42, "choice_id": [1, 2]},
    )
