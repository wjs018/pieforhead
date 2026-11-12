import asyncio
from unittest.mock import AsyncMock, Mock

from pieforhead.private_message import PrivateMessageAsync


def make_private_message(response: dict | bool | None) -> tuple[PrivateMessageAsync, Mock]:
    """Make a mock PrivateMessageAsync class to return toy data."""
    client = Mock()
    client.request = AsyncMock(return_value=response)

    return PrivateMessageAsync(client), client


def test_list_all_params():
    async def run_test():
        response = {"private_messages": []}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.list(page=2, limit=10, unread_only=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="private_message/list",
            params={"page": 2, "limit": 10, "unread_only": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_defaults():
    async def run_test():
        response = {"private_messages": []}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.list() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="private_message/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_conversation_all_params():
    async def run_test():
        response = {"private_messages": []}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.get_conversation(conversation_id=42, page=2, limit=10) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="private_message/conversation",
            params={"conversation_id": 42, "page": 2, "limit": 10},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_get_conversation_defaults():
    async def run_test():
        response = {"private_messages": []}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.get_conversation(person_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="private_message/conversation",
            params={"person_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_leave_conversation():
    async def run_test():
        # This endpoint just returns True on success
        response = True
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.leave_conversation(conversation_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="private_message/conversation/leave",
            data={"conversation_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_create():
    async def run_test():
        response = {"private_message_view": {}}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.create(content="Hello, world!", recipient_id=42) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="private_message",
            data={"content": "Hello, world!", "recipient_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_edit():
    async def run_test():
        response = {"private_message_view": {}}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.edit(content="Goodbye, world!", private_message_id=13) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="private_message",
            data={"private_message_id": 13, "content": "Goodbye, world!"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_mark_as_read():
    async def run_test():
        response = {"private_message_view": {}}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.mark_as_read(private_message_id=13, read=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="private_message/mark_as_read",
            data={"private_message_id": 13, "read": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_delete():
    async def run_test():
        response = {"private_message_view": {}}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.delete(private_message_id=13, deleted=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="private_message/delete",
            data={"private_message_id": 13, "deleted": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_report():
    async def run_test():
        response = {"private_message_report_view": {}}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.report(private_message_id=13, reason="Spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="private_message/report",
            data={"private_message_id": 13, "reason": "Spam"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_report_conversation():
    async def run_test():
        # This endpoint just returns True on success
        response = True
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.report_conversation(conversation_id=42, reason="Spam") == response

        # Check args
        client.request.assert_awaited_once_with(
            method="POST",
            endpoint="private_message/conversation/report",
            data={"conversation_id": 42, "reason": "Spam"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_reports_all_params():
    async def run_test():
        response = {"private_message_reports": []}
        private_message, client = make_private_message(response)

        # Check response
        assert (
            await private_message.list_reports(
                conversation_id=42,
                private_message_id=84,
                limit=10,
                page=2,
                unresolved_only=False,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="private_message/report/list",
            params={
                "conversation_id": 42,
                "private_message_id": 84,
                "limit": 10,
                "page": 2,
                "unresolved_only": False,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_reports_defaults():
    async def run_test():
        response = {"private_message_reports": []}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.list_reports() == response

        # Check args
        client.request.assert_awaited_once_with(method="GET", endpoint="private_message/report/list", params={})

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_conversation_reports_all_params():
    async def run_test():
        response = {"conversation_reports": []}
        private_message, client = make_private_message(response)

        # Check response
        assert (
            await private_message.list_conversation_reports(
                conversation_id=42,
                limit=10,
                page=2,
                unresolved_only=False,
                message_history_limit=5,
            )
            == response
        )

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="private_message/conversation/report/list",
            params={
                "conversation_id": 42,
                "limit": 10,
                "page": 2,
                "unresolved_only": False,
                "message_history_limit": 5,
            },
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_conversation_reports_defaults():
    async def run_test():
        response = {"conversation_reports": []}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.list_conversation_reports() == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="private_message/conversation/report/list",
            params={},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_resolve_report():
    async def run_test():
        response = {"private_message_report_view": {}}
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.resolve_report(report_id=2, resolved=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="private_message/report/resolve",
            data={"report_id": 2, "resolved": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_resolve_conversation_report():
    async def run_test():
        # This endpoint just returns True on success
        response = True
        private_message, client = make_private_message(response)

        # Check response
        assert await private_message.resolve_conversation_report(report_id=2, resolved=False) == response

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="private_message/conversation/report/resolve",
            data={"report_id": 2, "resolved": False},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())