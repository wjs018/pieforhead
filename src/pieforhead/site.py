from .clients import PieFedClient, AsyncPieFedClient
from .exceptions import NotImplementedError


class Site:
    """Class to hold Site endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def get(self) -> dict | None:
        """Dumps value returned from site endpoint into a dict.

        Returns:
            dict | None : contents of GET site endpoint, None if a suppressed error
        """

        return self._client.request(method="GET", endpoint="site")

    def version(self) -> dict | None:
        """Fetch software version from site/version endpoint.

        Returns:
            dict | None : response dict or none if an error was suppressed
        """

        return self._client.request(method="GET", endpoint="site/version")

    def block(self, block: bool, instance_id: int) -> dict | None:
        """Block or unblock an instance with a given id.

        Args:
            block (bool): True = block, False = unblock
            instance_id (int): id of instance

        Returns:
            dict | None : response dict or None if there was a suppressed error
        """
        payload = {"block": block, "instance_id": instance_id}

        return self._client.request(method="POST", endpoint="site/block", data=payload)

    def instance_chooser(self):
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    def instance_chooser_search(self):
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return


class SiteAsync:
    """Class to hold async Site endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def get(self) -> dict | None:
        """Dumps value returned from site endpoint into a dict.

        Returns:
            dict: contents of GET site endpoint
        """

        return await self._client.request(method="GET", endpoint="site")

    async def version(self) -> dict | None:
        """Fetch software version from site/version endpoint.

        Returns:
            dict | None : response dict or None if there was a suppressed error
        """

        return await self._client.request(method="GET", endpoint="site/version")

    async def block(self, block: bool, instance_id: int) -> dict | None:
        """Block or unblock an instance with a given id.

        Args:
            block (bool): True = block, False = unblock
            instance_id (int): id of instance

        Returns:
            dict | None : response dict or None if there was a suppressed error
        """
        payload = {"block": block, "instance_id": instance_id}

        return await self._client.request(method="POST", endpoint="site/block", data=payload)

    async def instance_chooser(self):
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    async def instance_chooser_search(self):
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return
