from unittest.mock import Mock

from pieforhead.private_message import PrivateMessage


def make_private_message(response: dict | bool | None) -> tuple[PrivateMessage, Mock]:
    """Make a mock PrivateMessage class to return toy data."""
    client = Mock()
    client.request.return_value = response

    return PrivateMessage(client), client


def test_list_all_params():
    response = {"private_messages": []}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.list_messages(page=2, limit=10, unread_only=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="private_message/list",
        params={"page": 2, "limit": 10, "unread_only": False},
    )


def test_list_defaults():
    response = {"private_messages": []}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.list_messages() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="private_message/list", params={})


def test_get_conversation_all_params():
    response = {"private_messages": []}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.get_conversation(conversation_id=42, page=2, limit=10) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="private_message/conversation",
        params={"conversation_id": 42, "page": 2, "limit": 10},
    )


def test_get_conversation_defaults():
    response = {"private_messages": []}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.get_conversation(person_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="private_message/conversation",
        params={"person_id": 42},
    )


def test_leave_conversation():
    # This endpoint just returns True on success
    response = True
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.leave_conversation(conversation_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="private_message/conversation/leave",
        data={"conversation_id": 42},
    )


def test_create():
    response = {"private_message_view": {}}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.create(content="Hello, world!", recipient_id=42) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="private_message",
        data={"content": "Hello, world!", "recipient_id": 42},
    )


def test_edit():
    response = {"private_message_view": {}}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.edit(content="Goodbye, world!", private_message_id=13) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="private_message",
        data={"private_message_id": 13, "content": "Goodbye, world!"},
    )


def test_mark_as_read():
    response = {"private_message_view": {}}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.mark_as_read(private_message_id=13, read=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="private_message/mark_as_read",
        data={"private_message_id": 13, "read": False},
    )


def test_delete():
    response = {"private_message_view": {}}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.delete(private_message_id=13, deleted=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="private_message/delete",
        data={"private_message_id": 13, "deleted": False},
    )


def test_report():
    response = {"private_message_report_view": {}}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.report(private_message_id=13, reason="Spam") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="private_message/report",
        data={"private_message_id": 13, "reason": "Spam"},
    )


def test_report_conversation():
    # This endpoint just returns True on success
    response = True
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.report_conversation(conversation_id=42, reason="Spam") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="private_message/conversation/report",
        data={"conversation_id": 42, "reason": "Spam"},
    )


def test_list_reports_all_params():
    response = {"private_message_reports": []}
    private_message, client = make_private_message(response)

    # Check response
    assert (
        private_message.list_reports(
            conversation_id=42,
            private_message_id=84,
            limit=10,
            page=2,
            unresolved_only=False,
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
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


def test_list_reports_defaults():
    response = {"private_message_reports": []}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.list_reports() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="private_message/report/list", params={})


def test_list_conversation_reports_all_params():
    response = {"conversation_reports": []}
    private_message, client = make_private_message(response)

    # Check response
    assert (
        private_message.list_conversation_reports(
            conversation_id=42,
            limit=10,
            page=2,
            unresolved_only=False,
            message_history_limit=5,
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
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


def test_list_conversation_reports_defaults():
    response = {"conversation_reports": []}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.list_conversation_reports() == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="private_message/conversation/report/list",
        params={},
    )


def test_resolve_report():
    response = {"private_message_report_view": {}}
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.resolve_report(report_id=2, resolved=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="private_message/report/resolve",
        data={"report_id": 2, "resolved": False},
    )


def test_resolve_conversation_report():
    # This endpoint just returns True on success
    response = True
    private_message, client = make_private_message(response)

    # Check response
    assert private_message.resolve_conversation_report(report_id=2, resolved=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="private_message/conversation/report/resolve",
        data={"report_id": 2, "resolved": False},
    )
