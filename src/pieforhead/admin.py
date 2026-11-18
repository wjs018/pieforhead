from .clients import PieFedClient, AsyncPieFedClient
from .exceptions import AdminException


class Admin:
    """Class to hold Admin endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list_applications(
        self,
        limit: int | None = None,
        page: int | None = None,
        pending_only: bool | None = None,
        sort: str | None = None,
    ) -> dict | None:
        """List applications to join the instance.

        API endpoint: GET admin/registration_application/list

        Args:
            limit (int | None, optional): Max number of applications to return. Defaults to None.
            page (int | None, optional): Page of results to request. Defaults to None.
            pending_only (bool | None, optional): Only return applications pending a decision. Defaults to None.
            sort (str | None, optional): One of "Old" or "New". Defaults to None.

        Returns:
            dict | None: Returns server json if request successful. None if there was an error but exceptions were
                ignored.
        """

        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if pending_only is not None:
            params["pending_only"] = pending_only
        if sort is not None:
            params["sort"] = sort

        return self._client.request(method="GET", endpoint="admin/registration_application/list", params=params)

    def process_application(self, approve: bool, new_user_id: int) -> bool | None:
        """Approve or reject an application.

        API endpoint: PUT admin/registration_application/approve

        Args:
            approve (bool): True to approve, False to reject.
            new_user_id (int): user_id of the applicant.

        Raises:
            AdminException: raised when the server responded in an unexpected way

        Returns:
            bool | None: Returns True on successful processing. Will return None if an exception occurred and was
                suppressed.
        """

        data = {"approve": approve, "user_id": new_user_id}

        resp = self._client.request(method="PUT", endpoint="admin/registration_application/approve", data=data)

        if resp is None:
            # Some problem with the request, but exceptions are suppressed
            return

        if not isinstance(resp, bool) or resp is False:
            if self._client.raise_exceptions:
                raise AdminException(f"Incorrect type returned from response: {type(resp)}")
            else:
                return

        return resp


class AdminAsync:
    """Class to hold async Admin endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def list_applications(
        self,
        limit: int | None = None,
        page: int | None = None,
        pending_only: bool | None = None,
        sort: str | None = None,
    ) -> dict | None:
        """List applications to join the instance.

        API endpoint: GET admin/registration_application/list

        Args:
            limit (int | None, optional): Max number of applications to return. Defaults to None.
            page (int | None, optional): Page of results to request. Defaults to None.
            pending_only (bool | None, optional): Only return applications pending a decision. Defaults to None.
            sort (str | None, optional): One of "Old" or "New". Defaults to None.

        Returns:
            dict | None: Returns server json if request successful. None if there was an error but exceptions were
                ignored.
        """

        params = {}
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if pending_only is not None:
            params["pending_only"] = pending_only
        if sort is not None:
            params["sort"] = sort

        return await self._client.request(method="GET", endpoint="admin/registration_application/list", params=params)

    async def process_application(self, approve: bool, new_user_id: int) -> bool | None:
        """Approve or reject an application.

        API endpoint: PUT admin/registration_application/approve

        Args:
            approve (bool): True to approve, False to reject.
            new_user_id (int): user_id of the applicant.

        Raises:
            AdminException: raised when the server responded in an unexpected way

        Returns:
            bool | None: Returns True on successful processing. Will return None if an exception occurred and was
                suppressed.
        """

        data = {"approve": approve, "user_id": new_user_id}

        resp = await self._client.request(method="PUT", endpoint="admin/registration_application/approve", data=data)

        if resp is None:
            # Some problem with the request, but exceptions are suppressed
            return

        if not isinstance(resp, bool) or resp is False:
            if self._client.raise_exceptions:
                raise AdminException(f"Incorrect type returned from response: {type(resp)}")
            else:
                return

        return resp
