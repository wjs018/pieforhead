from unittest.mock import Mock

from pieforhead.community import Community


def make_community(response: dict | bool | None) -> tuple[Community, Mock]:
    """Make a mock Community class to return toy data."""
    client = Mock()
    client.request.return_value = response

    return Community(client), client


def test_get_all_params():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.get(community_id=42, name="python") == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="community",
        params={"id": 42, "name": "python"},
    )


def test_get_defaults():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.get() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="community", params={})


def test_create_all_params():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert (
        community.create(
            name="python",
            title="Python",
            banner_url="https://site.tld/banner.png",
            description="Python community",
            discussion_languages=[1, 2],
            icon_url="https://site.tld/icon.png",
            local_only=False,
            nsfw=False,
            question_answer=True,
            restricted_to_mods=False,
            rules="Be kind",
        )
        == response
    )
    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community",
        data={
            "name": "python",
            "title": "Python",
            "banner_url": "https://site.tld/banner.png",
            "description": "Python community",
            "discussion_languages": [1, 2],
            "icon_url": "https://site.tld/icon.png",
            "local_only": False,
            "nsfw": False,
            "question_answer": True,
            "restricted_to_mods": False,
            "rules": "Be kind",
        },
    )


def test_create_defaults():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.create(name="python", title="Python") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community",
        data={"name": "python", "title": "Python"},
    )


def test_create_nullable_fields():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.create(name="python", title="Python", banner_url="", icon_url="") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community",
        data={"name": "python", "title": "Python", "banner_url": None, "icon_url": None},
    )


def test_edit_all_params():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert (
        community.edit(
            community_id=42,
            title="Python!",
            banner_url="https://site.tld/banner.png",
            description="Python community",
            discussion_languages=[1, 2],
            icon_url="https://site.tld/icon.png",
            local_only=False,
            nsfw=False,
            restricted_to_mods=False,
            question_answer=True,
            rules="Be kind",
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="community",
        data={
            "community_id": 42,
            "title": "Python!",
            "banner_url": "https://site.tld/banner.png",
            "description": "Python community",
            "discussion_languages": [1, 2],
            "icon_url": "https://site.tld/icon.png",
            "local_only": False,
            "nsfw": False,
            "restricted_to_mods": False,
            "question_answer": True,
            "rules": "Be kind",
        },
    )


def test_edit_defaults():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.edit(community_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="community",
        data={"community_id": 42},
    )


def test_edit_nullable_fields():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.edit(community_id=42, banner_url="", icon_url="") == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="community",
        data={"community_id": 42, "banner_url": None, "icon_url": None},
    )


def test_list_all_params():
    response = {"communities": []}
    community, client = make_community(response)

    # Check response
    assert community.list(limit=20, page=2, show_nsfw=False, sort="New", type_="Local") == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="community/list",
        params={"limit": 20, "page": 2, "show_nsfw": False, "sort": "New", "type_": "Local"},
    )


def test_list_defaults():
    response = {"communities": []}
    community, client = make_community(response)

    # Check response
    assert community.list() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="community/list", params={})


def test_follow():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.follow(community_id=42, follow=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/follow",
        data={"community_id": 42, "follow": False},
    )


def test_leave_all():
    response = {"local_user_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.leave_all() == response

    # Check args
    client.request.assert_called_once_with(method="POST", endpoint="community/leave_all")


def test_block():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.block(community_id=42, block=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/block",
        data={"community_id": 42, "block": False},
    )


def test_subscribe():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.subscribe(community_id=42, subscribe=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="community/subscribe",
        data={"community_id": 42, "subscribe": False},
    )


def test_delete():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.delete(community_id=42, deleted=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/delete",
        data={"community_id": 42, "deleted": False},
    )


def test_mod():
    response = {"moderators": []}
    community, client = make_community(response)

    # Check response
    assert community.mod(community_id=42, person_id=84, added=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/mod",
        data={"community_id": 42, "person_id": 84, "added": False},
    )


def test_list_bans_all_params():
    response = {"items": []}
    community, client = make_community(response)

    # Check response
    assert community.list_bans(community_id=42, limit=10, page=2) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="community/moderate/bans",
        params={"community_id": 42, "limit": 10, "page": 2},
    )


def test_list_bans_defaults():
    response = {"banned": []}
    community, client = make_community(response)

    # Check response
    assert community.list_bans(community_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="community/moderate/bans",
        params={"community_id": 42},
    )


def test_unban():
    response = {"banned_user": {}}
    community, client = make_community(response)

    # Check response
    assert community.unban(community_id=42, user_id=84) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="community/moderate/unban",
        data={"community_id": 42, "user_id": 84},
    )


def test_ban_user_all_params():
    response = {"banned_user": {}}
    community, client = make_community(response)

    # Check response
    assert (
        community.ban_user(
            community_id=42,
            user_id=84,
            reason="Spam",
            expires_at="2026-11-12T00:00:00Z",
            permanent=False,
        )
        == response
    )
    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/moderate/ban",
        data={
            "community_id": 42,
            "user_id": 84,
            "reason": "Spam",
            "expires_at": "2026-11-12T00:00:00Z",
            "permanent": False,
        },
    )


def test_ban_user_defaults():
    response = {"banned_user": {}}
    community, client = make_community(response)

    # Check response
    assert community.ban_user(community_id=42, user_id=84, reason="Spam") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/moderate/ban",
        data={"community_id": 42, "user_id": 84, "reason": "Spam"},
    )


def test_moderate_post_nsfw():
    response = {"post": {}}
    community, client = make_community(response)

    # Check response
    assert community.moderate_post_nsfw(post_id=42, nsfw_status=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/moderate/post/nsfw",
        data={"post_id": 42, "nsfw_status": False},
    )


def test_create_flair_all_params():
    response = {"flair_title": "Python"}
    community, client = make_community(response)

    # Check response
    assert (
        community.create_flair(
            community_id=42,
            flair_title="Python",
            text_color="#FFFFFF",
            background_color="#000000",
            blur_images=False,
        )
        == response
    )
    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/flair",
        data={
            "community_id": 42,
            "flair_title": "Python",
            "text_color": "#FFFFFF",
            "background_color": "#000000",
            "blur_images": False,
        },
    )


def test_create_flair_defaults():
    response = {"flair_title": "Python"}
    community, client = make_community(response)

    # Check response
    assert community.create_flair(community_id=42, flair_title="Python") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/flair",
        data={"community_id": 42, "flair_title": "Python"},
    )


def test_edit_flair_all_params():
    response = {"flair_title": "Python"}
    community, client = make_community(response)

    # Check response
    assert (
        community.edit_flair(
            flair_id=7,
            flair_title="Python",
            text_color="#FFFFFF",
            background_color="#000000",
            blur_images=False,
        )
        == response
    )
    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="community/flair",
        data={
            "flair_id": 7,
            "flair_title": "Python",
            "text_color": "#FFFFFF",
            "background_color": "#000000",
            "blur_images": False,
        },
    )


def test_edit_flair_defaults():
    response = {"flair_title": "Python"}
    community, client = make_community(response)

    # Check response
    assert community.edit_flair(flair_id=7) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="community/flair",
        data={"flair_id": 7},
    )


def test_delete_flair():
    response = {"community_view": {}}
    community, client = make_community(response)

    # Check response
    assert community.delete_flair(flair_id=7) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="community/flair/delete",
        data={"flair_id": 7},
    )
