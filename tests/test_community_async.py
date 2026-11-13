import asyncio
from unittest.mock import AsyncMock, Mock

from pieforhead.community import CommunityAsync


def make_community(response: dict | bool | None) -> tuple[CommunityAsync, Mock]:
    """Make a mock CommunityAsync class to return toy data."""
    client = Mock()
    client.request = AsyncMock(return_value=response)

    return CommunityAsync(client), client


def test_get_all_params():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.get(community_id=42, name="python") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="community",
            params={"id": 42, "name": "python"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_defaults():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.get() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="community", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_all_params():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert (
            await community.create(
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
        client.request.assert_awaited_once_with(
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

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_defaults():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.create(name="python", title="Python") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community",
            data={"name": "python", "title": "Python"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_nullable_fields():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.create(name="python", title="Python", banner_url="", icon_url="") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community",
            data={"name": "python", "title": "Python", "banner_url": None, "icon_url": None},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_all_params():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert (
            await community.edit(
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
        client.request.assert_awaited_once_with(
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

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_defaults():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.edit(community_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="community",
            data={"community_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_nullable_fields():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.edit(community_id=42, banner_url="", icon_url="") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="community",
            data={"community_id": 42, "banner_url": None, "icon_url": None},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_all_params():
    async def run_test():
        response = {"communities": []}
        community, client = make_community(response)

        # Check response
        assert await community.list(limit=20, page=2, show_nsfw=False, sort="New", type_="Local") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="community/list",
            params={"limit": 20, "page": 2, "show_nsfw": False, "sort": "New", "type_": "Local"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_defaults():
    async def run_test():
        response = {"communities": []}
        community, client = make_community(response)

        # Check response
        assert await community.list() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="community/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_follow():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.follow(community_id=42, follow=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/follow",
            data={"community_id": 42, "follow": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_leave_all():
    async def run_test():
        response = {"local_user_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.leave_all() == response

        # Check args
        client.request.assert_awaited_once_with(method="POST", endpoint="community/leave_all")

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_block():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.block(community_id=42, block=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/block",
            data={"community_id": 42, "block": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_subscribe():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.subscribe(community_id=42, subscribe=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="community/subscribe",
            data={"community_id": 42, "subscribe": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.delete(community_id=42, deleted=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/delete",
            data={"community_id": 42, "deleted": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_mod():
    async def run_test():
        response = {"moderators": []}
        community, client = make_community(response)

        # Check response
        assert await community.mod(community_id=42, person_id=84, added=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/mod",
            data={"community_id": 42, "person_id": 84, "added": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_bans_all_params():
    async def run_test():
        response = {"items": []}
        community, client = make_community(response)

        # Check response
        assert await community.list_bans(community_id=42, limit=10, page=2) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="community/moderate/bans",
            params={"community_id": 42, "limit": 10, "page": 2},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_bans_defaults():
    async def run_test():
        response = {"banned": []}
        community, client = make_community(response)

        # Check response
        assert await community.list_bans(community_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="community/moderate/bans",
            params={"community_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_unban():
    async def run_test():
        response = {"banned_user": {}}
        community, client = make_community(response)

        # Check response
        assert await community.unban(community_id=42, user_id=84) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="community/moderate/unban",
            data={"community_id": 42, "user_id": 84},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_ban_user_all_params():
    async def run_test():
        response = {"banned_user": {}}
        community, client = make_community(response)

        # Check response
        assert (
            await community.ban_user(
                community_id=42,
                user_id=84,
                reason="Spam",
                expires_at="2026-11-12T00:00:00Z",
                permanent=False,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
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

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_ban_user_defaults():
    async def run_test():
        response = {"banned_user": {}}
        community, client = make_community(response)

        # Check response
        assert await community.ban_user(community_id=42, user_id=84, reason="Spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/moderate/ban",
            data={"community_id": 42, "user_id": 84, "reason": "Spam"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_moderate_post_nsfw():
    async def run_test():
        response = {"post": {}}
        community, client = make_community(response)

        # Check response
        assert await community.moderate_post_nsfw(post_id=42, nsfw_status=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/moderate/post/nsfw",
            data={"post_id": 42, "nsfw_status": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_flair_all_params():
    async def run_test():
        response = {"flair_title": "Python"}
        community, client = make_community(response)

        # Check response
        assert (
            await community.create_flair(
                community_id=42,
                flair_title="Python",
                text_color="#FFFFFF",
                background_color="#000000",
                blur_images=False,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
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

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_flair_defaults():
    async def run_test():
        response = {"flair_title": "Python"}
        community, client = make_community(response)

        # Check response
        assert await community.create_flair(community_id=42, flair_title="Python") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/flair",
            data={"community_id": 42, "flair_title": "Python"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_flair_all_params():
    async def run_test():
        response = {"flair_title": "Python"}
        community, client = make_community(response)

        # Check response
        assert (
            await community.edit_flair(
                flair_id=7,
                flair_title="Python",
                text_color="#FFFFFF",
                background_color="#000000",
                blur_images=False,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
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

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_flair_defaults():
    async def run_test():
        response = {"flair_title": "Python"}
        community, client = make_community(response)

        # Check response
        assert await community.edit_flair(flair_id=7) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="community/flair",
            data={"flair_id": 7},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete_flair():
    async def run_test():
        response = {"community_view": {}}
        community, client = make_community(response)

        # Check response
        assert await community.delete_flair(flair_id=7) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="community/flair/delete",
            data={"flair_id": 7},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())
