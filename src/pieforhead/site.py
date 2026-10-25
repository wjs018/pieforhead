import semver

from .clients import PieFedClient, AsyncPieFedClient
from .exceptions import NotImplementedError, SiteException


class Site:
    """Class to hold Site endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def get(self) -> dict:
        """Dumps value returned from site endpoint into a dict.

        Returns:
            dict: contents of GET site endpoint
        """

        return self._client.request(method="GET", endpoint="site")

    def version(self) -> semver.Version:
        """Fetch software version from site/version endpoint.

        Returns:
            semver.Version: software version
        """

        resp = self._client.request(method="GET", endpoint="site/version")

        if "version" in resp:
            try:
                return semver.Version.parse(resp["version"])
            except ValueError as e:
                raise SiteException(f"Version not parseable: {resp['version']}") from e

        return

    def block(self, block: bool, instance_id: int) -> bool:
        """Block or unblock an instance with a given id.

        Args:
            block (bool): True = block, False = unblock
            instance_id (int): id of instance

        Returns:
            bool: True if instance is now blocked, False if it is now unblocked
        """
        payload = {"block": block, "instance_id": instance_id}

        resp = self._client.request(method="POST", endpoint="site/block", data=payload)

        return resp["blocked"]

    def instance_chooser(self):
        raise NotImplementedError

    def instance_chooser_search(self):
        raise NotImplementedError


class SiteAsync:
    """Class to hold async Site endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def get(self) -> dict:
        """Dumps value returned from site endpoint into a dict.

        Returns:
            dict: contents of GET site endpoint
        """

        return await self._client.request(method="GET", endpoint="site")

    async def version(self) -> semver.Version:
        """Fetch software version from site/version endpoint.

        Returns:
            semver.Version: software version
        """

        resp = await self._client.request(method="GET", endpoint="site/version")

        if "version" in resp:
            try:
                return semver.Version.parse(resp["version"])
            except ValueError as e:
                raise SiteException(f"Version not parseable: {resp['version']}") from e

        return

    async def block(self, block: bool, instance_id: int) -> bool:
        """Block or unblock an instance with a given id.

        Args:
            block (bool): True = block, False = unblock
            instance_id (int): id of instance

        Returns:
            bool: True if instance is now blocked, False if it is now unblocked
        """
        payload = {"block": block, "instance_id": instance_id}

        resp = await self._client.request(method="POST", endpoint="site/block", data=payload)

        return resp["blocked"]

    async def instance_chooser(self):
        raise NotImplementedError

    async def instance_chooser_search(self):
        raise NotImplementedError
