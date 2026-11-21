from .clients import PieFedClient, AsyncPieFedClient


class Blocklist:
    """Class to hold blocklist endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def get(self, id: int | None = None, name: str | None = None) -> dict | None:
        """Get the details of a single blocklist by name or id.

        API endpoint: GET blocklist

        Args:
            id (int | None, optional): Blocklist id to get info for. Defaults to None.
            name (str | None, optional): Blocklist name to get info for. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if id is not None:
            params["id"] = id
        if name is not None:
            params["name"] = name

        return self._client.request(method="GET", endpoint="blocklist", params=params)

    def create(self, name: str, title: str, description: str | None = None, members: str | None = None) -> dict | None:
        """Create a blocklist.

        API endpoint: POST blocklist

        Args:
            name (str): url-safe name.
            title (str): Display title.
            description (str | None, optional): Sidebar content in markdown. Defaults to None.
            members (str | None, optional): Newline separated list of blocked accounts. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"name": name, "title": title}

        if description is not None:
            data["description"] = description
        if members is not None:
            data["members"] = members

        return self._client.request(method="POST", endpoint="blocklist", data=data)

    def edit(
        self,
        blocklist_id: int,
        title: str | None = None,
        description: str | None = None,
        members: str | None = None,
    ) -> dict | None:
        """Edit a blocklist.

        API endpoint: PUT blocklist

        Args:
            blocklist_id (int): Blocklist id to edit.
            title (str | None, optional): Display title. Defaults to None.
            description (str | None, optional): Sidebar content in markdown. Defaults to None.
            members (str | None, optional): Newline separated list of blocked accounts. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"blocklist_id": blocklist_id}

        if title is not None:
            data["title"] = title
        if description is not None:
            data["description"] = description
        if members is not None:
            data["members"] = members

        return self._client.request(method="PUT", endpoint="blocklist", data=data)

    def list_blocklists(
        self,
        mine_only: bool | None = None,
        subscribed_only: bool | None = None,
        include_blocked: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict | None:
        """Get list of blocklists.

        API endpoint: GET blocklist/list

        Args:
            mine_only (bool | None, optional): Only return blocklists created by the logged-in user. Defaults to None.
            subscribed_only (bool | None, optional): Only return blocklists that the user is subscribed to. Defaults to
                None.
            include_blocked (bool | None, optional): Include the blocked accounts in the response. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if mine_only is not None:
            params["mine_only"] = mine_only
        if subscribed_only is not None:
            params["subscribed_only"] = subscribed_only
        if include_blocked is not None:
            params["include_blocked"] = include_blocked
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return self._client.request(method="GET", endpoint="blocklist/list", params=params)

    def follow(self, blocklist_id: int, follow: bool) -> dict | None:
        """Join or leave a blocklist.

        API endpoint: POST blocklist/follow

        Args:
            blocklist_id (int): Blocklist id to join or leave.
            follow (bool): True to join. False to leave.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"blocklist_id": blocklist_id, "follow": follow}

        return self._client.request(method="POST", endpoint="blocklist/follow", data=data)

    def delete(self, blocklist_id: int, deleted: bool) -> dict | None:
        """Delete or restore a blocklist.

        API endpoint: POST blocklist/delete

        Args:
            blocklist_id (int): Blocklist id to delete or restore.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"blocklist_id": blocklist_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="blocklist/delete", data=data)


class BlocklistAsync:
    """Class to hold async blocklist endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def get(self, id: int | None = None, name: str | None = None) -> dict | None:
        """Get the details of a single blocklist by name or id.

        API endpoint: GET blocklist

        Args:
            id (int | None, optional): Blocklist id to get info for. Defaults to None.
            name (str | None, optional): Blocklist name to get info for. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server.
        """
        params = {}

        if id is not None:
            params["id"] = id
        if name is not None:
            params["name"] = name

        return await self._client.request(method="GET", endpoint="blocklist", params=params)

    async def create(
        self, name: str, title: str, description: str | None = None, members: str | None = None
    ) -> dict | None:
        """Create a blocklist.

        API endpoint: POST blocklist

        Args:
            name (str): url-safe name.
            title (str): Display title.
            description (str | None, optional): Sidebar content in markdown. Defaults to None.
            members (str | None, optional): Newline separated list of blocked accounts. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server.
        """
        data = {"name": name, "title": title}

        if description is not None:
            data["description"] = description
        if members is not None:
            data["members"] = members

        return await self._client.request(method="POST", endpoint="blocklist", data=data)

    async def edit(
        self,
        blocklist_id: int,
        title: str | None = None,
        description: str | None = None,
        members: str | None = None,
    ) -> dict | None:
        """Edit a blocklist.

        API endpoint: PUT blocklist

        Args:
            blocklist_id (int): Blocklist id to edit.
            title (str | None, optional): Display title. Defaults to None.
            description (str | None, optional): Sidebar content in markdown. Defaults to None.
            members (str | None, optional): Newline separated list of blocked accounts. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server.
        """
        data = {"blocklist_id": blocklist_id}

        if title is not None:
            data["title"] = title
        if description is not None:
            data["description"] = description
        if members is not None:
            data["members"] = members

        return await self._client.request(method="PUT", endpoint="blocklist", data=data)

    async def list_blocklists(
        self,
        mine_only: bool | None = None,
        subscribed_only: bool | None = None,
        include_blocked: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict | None:
        """Get list of blocklists.

        API endpoint: GET blocklist/list

        Args:
            mine_only (bool | None, optional): Only return blocklists created by the logged-in user. Defaults to None.
            subscribed_only (bool | None, optional): Only return blocklists that the user is subscribed to. Defaults to
                None.
            include_blocked (bool | None, optional): Include the blocked accounts in the response. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server.
        """
        params = {}

        if mine_only is not None:
            params["mine_only"] = mine_only
        if subscribed_only is not None:
            params["subscribed_only"] = subscribed_only
        if include_blocked is not None:
            params["include_blocked"] = include_blocked
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="blocklist/list", params=params)

    async def follow(self, blocklist_id: int, follow: bool) -> dict | None:
        """Join or leave a blocklist.

        API endpoint: POST blocklist/follow

        Args:
            blocklist_id (int): Blocklist id to join or leave.
            follow (bool): True to join. False to leave.

        Returns:
            dict | None: dict containing the deserialized json returned by the server.
        """
        data = {"blocklist_id": blocklist_id, "follow": follow}

        return await self._client.request(method="POST", endpoint="blocklist/follow", data=data)

    async def delete(self, blocklist_id: int, deleted: bool) -> dict | None:
        """Delete or restore a blocklist.

        API endpoint: POST blocklist/delete

        Args:
            blocklist_id (int): Blocklist id to delete or restore.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server.
        """
        data = {"blocklist_id": blocklist_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="blocklist/delete", data=data)
