import json

import httpx
import pytest
import semver

from pieforhead.clients import PieFedClient
from pieforhead.exceptions import PieFedClientException


def make_client(handler, raise_exceptions=True):
    """Makes a mock client for testing.

    Args:
        handler: each test has a custom handler meant to give a specific, mocked response
        raise_exceptions: whether request errors should raise an exception

    Returns:
        PieFedClient: mocked client for testing
    """
    transport = httpx.MockTransport(handler)
    instance_url = "https://site.tld"
    api_version = "alpha"
    http_client = httpx.Client(
        transport=transport,
        base_url=f"{instance_url}/api/{api_version}/",
    )
    return PieFedClient(
        instance_url=instance_url,
        existing_client=http_client,
        raise_exceptions=raise_exceptions,
    )


def test_get_request():
    def custom_handler(request):
        # Test request things
        assert request.method == "GET"  # correct http method
        assert request.url.path == "/api/alpha/user"  # correct endpoint
        assert request.url.params["person_id"] == "42"  # correct url parameter
        return httpx.Response(200, json={"name": "foo"})  # return toy data

    client = make_client(custom_handler)

    try:
        resp = client.request("GET", "user", params={"person_id": 42})
        # Test response
        assert resp == {"name": "foo"}
    finally:
        client.close()


def test_request_with_empty_response_body():
    def custom_handler(request):
        # No json returned from server, but good status code
        return httpx.Response(200, text="null\n")

    client = make_client(custom_handler)

    try:
        # Test response
        assert client.request("GET", "site") is True
    finally:
        client.close()


# Test looks the same for both POST and PUT, so parametrize them
@pytest.mark.parametrize("method", ["POST", "PUT"])
def test_post_put_request(method: str):
    payload = {"name": "testing", "title": "Testing Community"}

    def custom_handler(request):
        # Test request things
        assert request.method == method  # correct http method
        assert request.url.path == "/api/alpha/community"  # correct endpoint
        assert json.loads(request.content) == payload  # correct json payload
        return httpx.Response(200, json={"community_id": 42})  # return toy data

    client = make_client(custom_handler)

    try:
        resp = client.request(method, "community", data=payload)
        # Test response
        assert resp == {"community_id": 42}
    finally:
        client.close()


def test_login_and_logout():
    def custom_handler(request):
        if request.url.path.endswith("/user/login"):
            # Login request, validate payload
            assert json.loads(request.content) == {"username": "test_user", "password": "hunter2"}
            return httpx.Response(200, json={"jwt": "test-token"})

        # Non-login request, empty response
        return httpx.Response(200, json={})

    client = make_client(custom_handler)

    try:
        # Logging in
        assert client.log_in("test_user", "hunter2") is True
        assert client.is_logged_in() is True  # confirming we are logged in
        assert client.current_username_or_email == "test_user"  # confirm username is saved
        assert client.current_password == "hunter2"  # confirm password is saved
        assert client.jwt_token == "test-token"  # confirm token is saved
        assert client.headers["Authorization"] == "Bearer test-token"  # confirm header is set

        # Logging out
        assert client.log_out() is True
        assert client.is_logged_in() is False  # confirm logging out
        assert client.jwt_token == ""  # confirm removing token
        assert client.current_username_or_email == ""  # confirm removing username
        assert client.current_password == ""  # confirm removing password
    finally:
        client.close()


def test_nodeinfo_and_version():
    num_requests = 0

    def custom_handler(request):
        nonlocal num_requests
        num_requests += 1

        assert request.url.path == "/nodeinfo/2.1.json"  # confirm proper url getting fetched
        return httpx.Response(200, json={"software": {"version": "1.2.3"}})

    client = make_client(custom_handler)

    try:
        assert num_requests == 0  # haven't made any request yet
        assert client.nodeinfo == {"software": {"version": "1.2.3"}}  # fetch the nodeinfo
        assert num_requests == 1  # first fetch issues a request
        assert client.nodeinfo == {"software": {"version": "1.2.3"}}  # subsequent call shouldn't issue request
        assert num_requests == 1  # still just the one request
        assert client.instance_version == semver.Version.parse("1.2.3")  # parse the version number
    finally:
        client.close()


def test_raise_exception_with_server_response():
    """Ensure that the server error message is passed along."""

    def custom_handler(request):
        return httpx.Response(400, json={"message": "Invalid request"})

    client = make_client(custom_handler)

    try:
        # Make sure that the mocked server error is included in the trace
        with pytest.raises(PieFedClientException, match=r"Invalid request"):
            client.request("GET", "site")
    finally:
        client.close()


def test_suppress_exceptions():
    """Ensure that server errors return None when exceptions are suppressed."""

    def custom_handler(request):
        return httpx.Response(400, json={"message": "Invalid request"})

    client = make_client(custom_handler, raise_exceptions=False)

    try:
        # No exception is raised and instead, the request just returns None
        assert client.request("GET", "site") is None
    finally:
        client.close()
