from unittest.mock import Mock

from pieforhead.misc import Misc


def make_misc(response: dict | None, raise_exceptions: bool = True) -> tuple[Misc, Mock]:
    """Make a mock Misc class to return toy data."""
    client = Mock()
    client.request.return_value = response
    client.raise_exceptions = raise_exceptions

    return Misc(client), client


def test_search():
    response = {"posts": [{"post_id": 42}]}
    misc, client = make_misc(response)

    # Check response
    assert misc.search(query="test", type_="Posts") == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="search",
        params={"q": "test", "type_": "Posts"},
    )


def test_search_optional_params():
    response = {"posts": [{"post_id": 42}]}
    misc, client = make_misc(response)

    # Check response
    assert (
        misc.search(
            query="test",
            type_="Posts",
            limit=10,
            listing_type="All",
            page=2,
            sort="New",
            community_name="python",
            community_id=3,
            minimum_upvotes=5,
            nsfw="false",
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="search",
        params={
            "q": "test",
            "type_": "Posts",
            "limit": 10,
            "listing_type": "All",
            "page": 2,
            "sort": "New",
            "community_name": "python",
            "community_id": 3,
            "minimum_upvotes": 5,
            "nsfw": "false",
        },
    )


def test_search_raising():
    # Make sure to return None if request returns None
    misc, client = make_misc(None, raise_exceptions=False)

    # Check response
    assert misc.search(query="test", type_="Posts") is None

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="search",
        params={"q": "test", "type_": "Posts"},
    )


def test_resolve_object():
    response = {"post": {"post_id": 42}}
    misc, client = make_misc(response)

    # Check response
    assert misc.resolve_object(query="https://site.tld/post/42") == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="resolve_object",
        params={"q": "https://site.tld/post/42"},
    )


def test_resolve_object_raising():
    # Make sure to return None if request returns None
    misc, client = make_misc(None, raise_exceptions=False)

    # Check response
    assert misc.resolve_object(query="https://site.tld/post/42") is None

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="resolve_object",
        params={"q": "https://site.tld/post/42"},
    )


def test_federated_instances():
    response = {"federated_instances": {"linked": [], "allowed": [], "blocked": []}}
    misc, client = make_misc(response)

    # Check response
    assert misc.federated_instances() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="federated_instances")


def test_federated_instances_raising():
    # Make sure to return None if request returns None
    misc, client = make_misc(None, raise_exceptions=False)

    # Check response
    assert misc.federated_instances() is None

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="federated_instances")


def test_suggest_completion():
    response = {"result": ["test_user1", "test_user2"]}
    misc, client = make_misc(response)

    # Check response
    assert misc.suggest_completion(query="@tes") == response

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="suggest_completion",
        params={"q": "@tes"},
    )


def test_suggest_completion_raising():
    # Make sure to return None if request returns None
    misc, client = make_misc(None, raise_exceptions=False)

    # Check response
    assert misc.suggest_completion(query="@tes") is None

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="suggest_completion",
        params={"q": "@tes"},
    )


def test_modlog():
    response = {"added": [{"mod_add": {"id": 42}}]}
    misc, client = make_misc(response)

    # Check response
    assert misc.modlog() == response

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="modlog", params={})


def test_modlog_non_default_posts():
    response = {"removed_posts": [{"mod_remove_post": {"id": 42}}]}
    misc, client = make_misc(response)

    # Check response
    assert (
        misc.modlog(
            mod_person_id=1,
            community_id=2,
            page=3,
            limit=20,
            type_="ModRemovePost",
            other_person_id=4,
            post_id=5,
            comment_id=6,
        )
        == response
    )

    # Check args
    client.request.assert_called_once_with(
        method="GET",
        endpoint="modlog",
        params={
            "mod_person_id": 1,
            "community_id": 2,
            "page": 3,
            "limit": 20,
            "type_": "ModRemovePost",
            "other_person_id": 4,
            "post_id": 5,
            "comment_id": 6,
        },
    )


def test_modlog_raising():
    # Make sure to return None if request returns None
    misc, client = make_misc(None, raise_exceptions=False)

    # Check response
    assert misc.modlog() is None

    # Check args
    client.request.assert_called_once_with(method="GET", endpoint="modlog", params={})
