import asyncio
import json

import httpx
import pytest
import semver

from pieforhead.clients import AsyncPieFedClient
from pieforhead.exceptions import PieFedClientException


def make_client(handler):
    """Makes a mock async client for testing.

    Args:
        handler: each test has a custom handler meant to give a specific, mocked response

    Returns:
        AsyncPieFedClient: mocked async client for testing
    """
    transport = httpx.MockTransport(handler)
    instance_url = "https://site.tld"
    api_version = "alpha"
    http_client = httpx.AsyncClient(
        transport=transport,
        base_url=f"{instance_url}/api/{api_version}/",
    )
    return AsyncPieFedClient(instance_url=instance_url, existing_client=http_client)


def test_get_request():
    async def run_test():
        def custom_handler(request):
            # Test request things
            assert request.method == "GET"  # correct http method
            assert request.url.path == "/api/alpha/user"  # correct endpoint
            assert request.url.params["person_id"] == "42"  # correct url parameter
            return httpx.Response(200, json={"name": "foo"})  # return toy data

        client = make_client(custom_handler)

        try:
            resp = await client.request("GET", "user", params={"person_id": 42})
            # Test response
            assert resp == {"name": "foo"}
        finally:
            await client.close()

    # Start the event loop and run the test
    asyncio.run(run_test())


# Test looks the same for both POST and PUT, so parametrize them
@pytest.mark.parametrize("method", ["POST", "PUT"])
def test_post_put_request(method: str):
    async def run_test():
        payload = {"name": "testing", "title": "Testing Community"}

        def custom_handler(request):
            # Test request things
            assert request.method == method  # correct http method
            assert request.url.path == "/api/alpha/community"  # correct endpoint
            assert json.loads(request.content) == payload  # correct json payload
            return httpx.Response(200, json={"community_id": 42})  # return toy data

        client = make_client(custom_handler)

        try:
            resp = await client.request(method, "community", data=payload)
            # Test response
            assert resp == {"community_id": 42}
        finally:
            await client.close()

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_login_and_logout():
    async def run_test():
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
            assert await client.log_in("test_user", "hunter2") is True
            assert await client.is_logged_in() is True  # confirming we are logged in
            assert client.current_username_or_email == "test_user"  # confirm username is saved
            assert client.current_password == "hunter2"  # confirm password is saved
            assert client.jwt_token == "test-token"  # confirm token is saved
            assert client.headers["Authorization"] == "Bearer test-token"  # confirm header is set

            # Logging out
            assert await client.log_out() is True
            assert await client.is_logged_in() is False  # confirm logging out
            assert client.jwt_token == ""  # confirm removing token
            assert client.current_username_or_email == ""  # confirm removing username
            assert client.current_password == ""  # confirm removing password
        finally:
            await client.close()

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_nodeinfo_and_version():
    async def run_test():
        num_requests = 0

        def custom_handler(request):
            nonlocal num_requests
            num_requests += 1

            assert request.url.path == "/nodeinfo/2.1.json"  # confirm proper url getting fetched
            return httpx.Response(200, json={"software": {"version": "1.2.3"}})

        client = make_client(custom_handler)

        try:
            assert num_requests == 0  # haven't made any request yet
            assert await client.nodeinfo == {"software": {"version": "1.2.3"}}  # fetch the nodeinfo
            assert num_requests == 1  # first fetch issues a request
            assert await client.nodeinfo == {
                "software": {"version": "1.2.3"}
            }  # subsequent call shouldn't issue request
            assert num_requests == 1  # still just the one request
            assert await client.instance_version == semver.Version.parse("1.2.3")  # parse the version number
        finally:
            await client.close()

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_raise_exception_with_server_response():
    """Ensure that the server error message is passed along."""

    async def run_test():
        def custom_handler(request):
            return httpx.Response(400, json={"message": "Invalid request"})

        client = make_client(custom_handler)

        try:
            # Make sure that the mocked server error is included in the trace
            with pytest.raises(PieFedClientException, match=r"Invalid request"):
                await client.request("GET", "site")
        finally:
            await client.close()

    # Start the event loop and run the test
    asyncio.run(run_test())
