import logging

import semver

from .clients import AsyncPieFedClient, PieFedClient
from .image import Image, ImageAsync
from .site import Site, SiteAsync
from .topic import Topic, TopicAsync
from .admin import Admin, AdminAsync
from .misc import Misc, MiscAsync

logger = logging.getLogger(__name__)


class PieFed:
    _client: PieFedClient
    instance_url: str

    def __init__(self, instance_url: str, timeout: float = 5.0, raise_exceptions: bool = True):
        self.instance_url = instance_url.removesuffix("/")
        self._client = PieFedClient(instance_url=instance_url, timeout=timeout, raise_exceptions=raise_exceptions)

        # Initialize attributes used for different endpoint groupings
        self.site = Site(client=self._client)
        self.image = Image(client=self._client)
        self.topic = Topic(client=self._client)
        self.admin = Admin(client=self._client)
        self.misc = Misc(client=self._client)

    def __enter__(self):
        return self

    def log_in(self, username_or_email: str, password: str) -> bool:
        return self._client.log_in(username_or_email, password)

    def is_logged_in(self) -> bool:
        return self._client.is_logged_in()

    def log_out(self) -> bool:
        return self._client.log_out()

    def close(self):
        self._client.close()

    def __exit__(self, *args):
        self.close()

    @property
    def instance_version(self) -> semver.Version:
        return self._client.instance_version


class PieFedAsync:
    _client: AsyncPieFedClient
    instance_url: str

    def __init__(self, instance_url: str, timeout: float = 5.0, raise_exceptions: bool = True):
        self.instance_url = instance_url.removesuffix("/")
        self._client = AsyncPieFedClient(instance_url=instance_url, timeout=timeout, raise_exceptions=raise_exceptions)

        # Initialize attributes used for different endpoint groupings
        self.site = SiteAsync(client=self._client)
        self.image = ImageAsync(client=self._client)
        self.topic = TopicAsync(client=self._client)
        self.admin = AdminAsync(client=self._client)
        self.misc = MiscAsync(client=self._client)

    async def __aenter__(self):
        return self

    async def log_in(self, username_or_email: str, password: str) -> bool:
        return await self._client.log_in(username_or_email, password)

    async def is_logged_in(self) -> bool:
        return await self._client.is_logged_in()

    async def log_out(self) -> bool:
        return await self._client.log_out()

    async def close(self):
        await self._client.close()

    async def __aexit__(self, *args):
        await self.close()

    @property
    async def instance_version(self) -> semver.Version:
        return await self._client.instance_version
