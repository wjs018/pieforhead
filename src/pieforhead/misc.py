from .clients import PieFedClient, AsyncPieFedClient


class Misc:
    """Class to hold Misc endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

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
        # Build our parameters, only including optional params that have been specified
        params = {"q": query, "type_": type_}

        if limit is not None:
            params["limit"] = limit
        if listing_type is not None:
            params["listing_type"] = listing_type
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if community_name is not None:
            params["community_name"] = community_name
        if community_id is not None:
            params["community_id"] = community_id
        if minimum_upvotes is not None:
            params["minimum_upvotes"] = minimum_upvotes
        if nsfw is not None:
            params["nsfw"] = nsfw

        return self._client.request(method="GET", endpoint="search", params=params)

    def resolve_object(self, query: str) -> dict | None:
        return self._client.request(method="GET", endpoint="resolve_object", params={"q": query})

    def federated_instances(self) -> dict | None:
        return self._client.request(method="GET", endpoint="federated_instances")

    def suggest_completion(self, query: str) -> dict | None:
        return self._client.request(method="GET", endpoint="suggest_completion", params={"q": query})

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
        # Build our params if provided
        params = {}
        if mod_person_id is not None:
            params["mod_person_id"] = mod_person_id
        if community_id is not None:
            params["community_id"] = community_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if type_ is not None:
            params["type_"] = type_
        if other_person_id is not None:
            params["other_person_id"] = other_person_id
        if post_id is not None:
            params["post_id"] = post_id
        if comment_id is not None:
            params["comment_id"] = comment_id

        return self._client.request(method="GET", endpoint="modlog", params=params)


class MiscAsync:
    """Class to hold async Misc endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

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
        # Build our parameters, only including optional params that have been specified
        params = {"q": query, "type_": type_}

        if limit is not None:
            params["limit"] = limit
        if listing_type is not None:
            params["listing_type"] = listing_type
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if community_name is not None:
            params["community_name"] = community_name
        if community_id is not None:
            params["community_id"] = community_id
        if minimum_upvotes is not None:
            params["minimum_upvotes"] = minimum_upvotes
        if nsfw is not None:
            params["nsfw"] = nsfw

        return await self._client.request(method="GET", endpoint="search", params=params)

    async def resolve_object(self, query: str) -> dict | None:
        return await self._client.request(method="GET", endpoint="resolve_object", params={"q": query})

    async def federated_instances(self) -> dict | None:
        return await self._client.request(method="GET", endpoint="federated_instances")

    async def suggest_completion(self, query: str) -> dict | None:
        return await self._client.request(method="GET", endpoint="suggest_completion", params={"q": query})

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
        params = {}
        if mod_person_id is not None:
            params["mod_person_id"] = mod_person_id
        if community_id is not None:
            params["community_id"] = community_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if type_ is not None:
            params["type_"] = type_
        if other_person_id is not None:
            params["other_person_id"] = other_person_id
        if post_id is not None:
            params["post_id"] = post_id
        if comment_id is not None:
            params["comment_id"] = comment_id

        return await self._client.request(method="GET", endpoint="modlog", params=params)
