import asyncio
from unittest.mock import AsyncMock, Mock

from pieforhead.blocklist import BlocklistAsync


def make_blocklist(response: dict | None) -> tuple[BlocklistAsync, Mock]:
    client = Mock()
    client.request = AsyncMock(return_value=response)
    return BlocklistAsync(client), client


def test_get_by_id():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert await blocklist.get(id=42) == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="blocklist", params={"id": 42})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_by_name():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert await blocklist.get(name="test@instance.tld") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="blocklist",
            params={"name": "test@instance.tld"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_all_fields():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert (
            await blocklist.create(
                name="example",
                title="Example blocklist",
                description="Accounts to block",
                members="user1@instance.tld\nuser2@instance.tld",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="blocklist",
            data={
                "name": "example",
                "title": "Example blocklist",
                "description": "Accounts to block",
                "members": "user1@instance.tld\nuser2@instance.tld",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create_few_fields():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert await blocklist.create(name="example", title="Example blocklist") is response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="blocklist",
            data={"name": "example", "title": "Example blocklist"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_all_fields():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert (
            await blocklist.edit(
                blocklist_id=42,
                title="Updated blocklist",
                description="Updated description",
                members="user@instance.tld",
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="blocklist",
            data={
                "blocklist_id": 42,
                "title": "Updated blocklist",
                "description": "Updated description",
                "members": "user@instance.tld",
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit_defaults():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert await blocklist.edit(blocklist_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(method="PUT", endpoint="blocklist", data={"blocklist_id": 42})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_blocklists_defaults():
    async def run_test():
        response = {"blocklists": []}
        blocklist, client = make_blocklist(response)

        # Check response
        assert await blocklist.list_blocklists() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="blocklist/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_blocklists_params():
    async def run_test():
        response = {"blocklists": []}
        blocklist, client = make_blocklist(response)

        # Check response
        assert (
            await blocklist.list_blocklists(
                mine_only=False,
                subscribed_only=True,
                include_blocked=False,
                page=2,
                limit=20,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="blocklist/list",
            params={
                "mine_only": False,
                "subscribed_only": True,
                "include_blocked": False,
                "page": 2,
                "limit": 20,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_follow():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert await blocklist.follow(blocklist_id=42, follow=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="blocklist/follow",
            data={"blocklist_id": 42, "follow": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete():
    async def run_test():
        response = {"id": 42}
        blocklist, client = make_blocklist(response)

        # Check response
        assert await blocklist.delete(blocklist_id=42, deleted=True) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="blocklist/delete",
            data={"blocklist_id": 42, "deleted": True},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())
