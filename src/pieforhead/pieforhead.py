import logging

import semver

from .clients import AsyncPieFedClient, PieFedClient
from .image import Image, ImageAsync
from .site import Site, SiteAsync
from .topic import Topic, TopicAsync
from .admin import Admin, AdminAsync
from .misc import Misc, MiscAsync
from .user import User, UserAsync
from .feed import Feed, FeedAsync

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
        self.user = User(client=self._client)
        self.feed = Feed(client=self._client)

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

    # Map Misc endpoints to the top-level PieFed object
    def search(
        self,
        query: str,
        type_: str,
        limit: int | None = None,
        listing_type: str | None = None,
        page: int | None = None,
        sort: str | None = None,
        community_name: str | None = None,
        community_id: int | None = None,
        minimum_upvotes: int | None = None,
        nsfw: str | None = None,
    ) -> dict | None:
        return self.misc.search(
            query=query,
            type_=type_,
            limit=limit,
            listing_type=listing_type,
            page=page,
            sort=sort,
            community_name=community_name,
            community_id=community_id,
            minimum_upvotes=minimum_upvotes,
            nsfw=nsfw,
        )

    def resolve_object(self, query: str) -> dict | None:
        return self.misc.resolve_object(query=query)

    def federated_instances(self) -> dict | None:
        return self.misc.federated_instances()

    def suggest_completion(self, query: str) -> dict | None:
        return self.misc.suggest_completion(query=query)

    def modlog(
        self,
        mod_person_id: int | None = None,
        community_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        type_: str | None = None,
        other_person_id: int | None = None,
        post_id: int | None = None,
        comment_id: int | None = None,
    ) -> dict | None:
        return self.misc.modlog(
            mod_person_id=mod_person_id,
            community_id=community_id,
            page=page,
            limit=limit,
            type_=type_,
            other_person_id=other_person_id,
            post_id=post_id,
            comment_id=comment_id,
        )


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
        self.user = UserAsync(client=self._client)
        self.feed = FeedAsync(client=self._client)

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

    # Map Misc endpoints to the top-level PieFedAsync object
    async def search(
        self,
        query: str,
        type_: str,
        limit: int | None = None,
        listing_type: str | None = None,
        page: int | None = None,
        sort: str | None = None,
        community_name: str | None = None,
        community_id: int | None = None,
        minimum_upvotes: int | None = None,
        nsfw: str | None = None,
    ) -> dict | None:
        return await self.misc.search(
            query=query,
            type_=type_,
            limit=limit,
            listing_type=listing_type,
            page=page,
            sort=sort,
            community_name=community_name,
            community_id=community_id,
            minimum_upvotes=minimum_upvotes,
            nsfw=nsfw,
        )

    async def resolve_object(self, query: str) -> dict | None:
        return await self.misc.resolve_object(query=query)

    async def federated_instances(self) -> dict | None:
        return await self.misc.federated_instances()

    async def suggest_completion(self, query: str) -> dict | None:
        return await self.misc.suggest_completion(query=query)

    async def modlog(
        self,
        mod_person_id: int | None = None,
        community_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        type_: str | None = None,
        other_person_id: int | None = None,
        post_id: int | None = None,
        comment_id: int | None = None,
    ) -> dict | None:
        return await self.misc.modlog(
            mod_person_id=mod_person_id,
            community_id=community_id,
            page=page,
            limit=limit,
            type_=type_,
            other_person_id=other_person_id,
            post_id=post_id,
            comment_id=comment_id,
        )
