from .clients import PieFedClient, AsyncPieFedClient
from .exceptions import AdminException


class Admin:
    """Class to hold Admin endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list_applications(
        self,
        limit: int = 30,
        page: int = 1,
        pending_only: bool = True,
        sort: str = "New",
    ) -> dict | None:
        """List applications to joint the instance.

        Args:
            limit (int, optional): Max number of applications to return. Defaults to 30.
            page (int, optional): Page of results to request. Defaults to 1.
            pending_only (bool, optional): Only return applications pending a decision. Defaults to True.
            sort (str, optional): One of "Old" or "New". Defaults to "New".

        Returns:
            dict | None: Returns server json if request successful. None if there was an error but exceptions were
                ignored.
        """

        params = {"limit": limit, "page": page, "pending_only": pending_only, "sort": sort}

        resp = self._client.request(method="GET", endpoint="admin/registration_application/list", params=params)

        if resp is None:
            # Some problem with the request, but exceptions are suppressed
            return

        return resp

    def process_application(self, approve: bool, new_user_id: int) -> bool | None:
        """Approve or reject an application.

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
        limit: int = 30,
        page: int = 1,
        pending_only: bool = True,
        sort: str = "New",
    ) -> dict | None:
        """List applications to joint the instance.

        Args:
            limit (int, optional): Max number of applications to return. Defaults to 30.
            page (int, optional): Page of results to request. Defaults to 1.
            pending_only (bool, optional): Only return applications pending a decision. Defaults to True.
            sort (str, optional): One of "Old" or "New". Defaults to "New".

        Returns:
            dict | None: Returns server json if request successful. None if there was an error but exceptions were
                ignored.
        """

        params = {"limit": limit, "page": page, "pending_only": pending_only, "sort": sort}

        resp = await self._client.request(method="GET", endpoint="admin/registration_application/list", params=params)

        if resp is None:
            # Some problem with the request, but exceptions are suppressed
            return

        return resp

    async def process_application(self, approve: bool, new_user_id: int) -> bool | None:
        """Approve or reject an application.

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
