import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from pieforhead.admin import AdminAsync
from pieforhead.exceptions import AdminException


def make_admin(response: dict | bool | None, raise_exceptions: bool = True) -> tuple[AdminAsync, Mock]:
    """Make a mock async Admin class to return toy data."""
    client = Mock()
    client.request = AsyncMock(return_value=response)
    client.raise_exceptions = raise_exceptions

    return AdminAsync(client), client


def test_list_applications():
    async def run_test():
        response = {"registrations": [{"user_id": 42}]}
        admin, client = make_admin(response)

        # Check response
        assert await admin.list_applications() == response

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="admin/registration_application/list",
            params={"limit": 30, "page": 1, "pending_only": True, "sort": "New"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_applications_params():
    async def run_test():
        response = {"registrations": [{"user_id": 42}]}
        admin, client = make_admin(response)

        # Check response
        assert await admin.list_applications(limit=10, page=2, pending_only=False, sort="Old") == response

        # Check to make sure params are not the defaults
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="admin/registration_application/list",
            params={"limit": 10, "page": 2, "pending_only": False, "sort": "Old"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_list_applications_raising():
    async def run_test():
        # A None value from request means that an error occurred that is being suppressed
        admin, client = make_admin(None, raise_exceptions=False)

        # Check response
        assert await admin.list_applications() is None

        # Check args
        client.request.assert_awaited_once_with(
            method="GET",
            endpoint="admin/registration_application/list",
            params={"limit": 30, "page": 1, "pending_only": True, "sort": "New"},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_process_application():
    async def run_test():
        # An empty 200 response from the server means just a True value returned from the request function
        admin, client = make_admin(True)

        # Check response
        assert await admin.process_application(approve=True, new_user_id=42) is True

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="admin/registration_application/approve",
            data={"approve": True, "user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_process_application_false_raising():
    async def run_test():
        # Make sure that our logic catches False bools correctly (something is wrong if False is returned from request)
        admin, client = make_admin(False)

        # Make sure exception is raised
        with pytest.raises(AdminException, match="Incorrect type returned from response"):
            await admin.process_application(approve=True, new_user_id=42)

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="admin/registration_application/approve",
            data={"approve": True, "user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_process_application_false_suppressing():
    async def run_test():
        # Make sure the exception is ignored in the weird case where the bool False is returned by request
        admin, client = make_admin(False, raise_exceptions=False)

        # Check response
        assert await admin.process_application(approve=True, new_user_id=42) is None

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="admin/registration_application/approve",
            data={"approve": True, "user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_process_application_none_returned():
    async def run_test():
        # A None value from request means that an error occurred that is being suppressed
        admin, client = make_admin(None, raise_exceptions=False)

        # Check response
        assert await admin.process_application(approve=True, new_user_id=42) is None

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="admin/registration_application/approve",
            data={"approve": True, "user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_process_application_wrong_type_raising():
    async def run_test():
        # Returning a non-bool non-NoneType value should raise an exception
        admin, client = make_admin({"result": "ok"})

        # Make sure exception is raised
        with pytest.raises(AdminException, match="Incorrect type returned from response"):
            await admin.process_application(approve=True, new_user_id=42)

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="admin/registration_application/approve",
            data={"approve": True, "user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())


def test_process_application_wrong_type_suppressing():
    async def run_test():
        # If ignoring exceptions, just return None when an invalid response comes from request
        admin, client = make_admin({"result": "ok"}, raise_exceptions=False)

        # Check response
        assert await admin.process_application(approve=True, new_user_id=42) is None

        # Check args
        client.request.assert_awaited_once_with(
            method="PUT",
            endpoint="admin/registration_application/approve",
            data={"approve": True, "user_id": 42},
        )

    # Start the event loop and run the test
    asyncio.run(run_test())
