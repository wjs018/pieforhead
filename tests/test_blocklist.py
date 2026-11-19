from unittest.mock import Mock

from pieforhead.blocklist import Blocklist


def make_blocklist(response: dict | None) -> tuple[Blocklist, Mock]:
    client = Mock()
    client.request.return_value = response
    return Blocklist(client), client


def test_get_by_id():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert blocklist.get(id=42) == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="blocklist", params={"id": 42})


def test_get_by_name():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert blocklist.get(name="test@instance.tld") == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="blocklist", params={"name": "test@instance.tld"})


def test_create_all_fields():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert (
        blocklist.create(
            name="example",
            title="Example blocklist",
            description="Accounts to block",
            members="user1@instance.tld\nuser2@instance.tld",
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="blocklist",
        data={
            "name": "example",
            "title": "Example blocklist",
            "description": "Accounts to block",
            "members": "user1@instance.tld\nuser2@instance.tld",
        },
    )


def test_create_few_fields():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert blocklist.create(name="example", title="Example blocklist") is response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="blocklist",
        data={"name": "example", "title": "Example blocklist"},
    )


def test_edit_all_fields():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert (
        blocklist.edit(
            blocklist_id=42,
            title="Updated blocklist",
            description="Updated description",
            members="user@instance.tld",
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
        method="PUT",
        endpoint="blocklist",
        data={
            "blocklist_id": 42,
            "title": "Updated blocklist",
            "description": "Updated description",
            "members": "user@instance.tld",
        },
    )


def test_edit_defaults():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert blocklist.edit(blocklist_id=42) == response

    # Check args
    client.request.assert_called_once_with(method="PUT", endpoint="blocklist", data={"blocklist_id": 42})


def test_list_blocklists_defaults():
    response = {"blocklists": []}
    blocklist, client = make_blocklist(response)

    # Check response
    assert blocklist.list_blocklists() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="blocklist/list", params={})


def test_list_blocklists_params():
    response = {"blocklists": []}
    blocklist, client = make_blocklist(response)

    # Check response
    assert (
        blocklist.list_blocklists(
            mine_only=False,
            subscribed_only=True,
            include_blocked=False,
            page=2,
            limit=20,
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
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


def test_follow():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert blocklist.follow(blocklist_id=42, follow=False) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="blocklist/follow",
        data={"blocklist_id": 42, "follow": False},
    )


def test_delete():
    response = {"id": 42}
    blocklist, client = make_blocklist(response)

    # Check response
    assert blocklist.delete(blocklist_id=42, deleted=True) == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="blocklist/delete",
        data={"blocklist_id": 42, "deleted": True},
    )
