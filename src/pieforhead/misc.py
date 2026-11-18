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
        """Search for content.

        API endpoint: GET search

        Args:
            query (str): Search string.
            type_ (str): Type of content to search for (Comments, Posts, etc.)
            limit (int | None, optional): Maximum items per page in the response. Defaults to None.
            listing_type (str | None, optional): Filter to apply (All, Local, etc.). See PieFed API docs for more info.
                Defaults to None.
            page (int | None, optional): The page number of results to request. Defaults to None.
            sort (str | None, optional): Sort method for the results (Old, New, etc.). Some sorts are only supported on
                certain type_'s. See the PieFed API docs for more info. Defaults to None.
            community_name (str | None, optional): Filter search to a specific community by name. Defaults to None.
            community_id (int | None, optional): Filter search to a specific community by id. Defaults to None.
            minimum_upvotes (int | None, optional): Filter results to only those above a certain number of upvotes.
                Defaults to None.
            nsfw (str | None, optional): How to filter NSFW results (Exclude, Include, Only). Defaults to None.

        Returns:
            dict | None: dict containing the json returned from the server. None is returned if an exception was raised
                and then subsequently ignored due to the client setting.
        """
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
        """Fetch an item from the server based on it's activitypub id.

        API endpoint: GET resolve_object

        Args:
            query (str): url of the item to resolve. If the item is not already federated to the instance, you will
                need to be authenticated.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="resolve_object", params={"q": query})

    def federated_instances(self) -> dict | None:
        """Get lists of instances and their federation status.

        API endpoint: GET federated_instances

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="federated_instances")

    def suggest_completion(self, query: str) -> dict | None:
        """Suggest autocompletions for users, communities, etc based on a partial string.

        API endpoint: GET suggest_completion

        Args:
            query (str): Partial username, community name, etc. Include leading character - @ for users, etc.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Fetch modlog entries.

        API endpoint: GET modlog

        Args:
            mod_person_id (int | None, optional): User id of the user doing the mod action. Defaults to None.
            community_id (int | None, optional): Community id in which action happened. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Number of items to return on the page of results. Defaults to None.
            type_ (str | None, optional): Filter by type of mod action. Defaults to None.
            other_person_id (int | None, optional): User id that mod action is directed towards. Defaults to None.
            post_id (int | None, optional): Post id of post that is being actioned. Defaults to None.
            comment_id (int | None, optional): Comment id of comment that is being actioned. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Search for content.

        API endpoint: GET search

        Args:
            query (str): Search string.
            type_ (str): Type of content to search for (Comments, Posts, etc.)
            limit (int | None, optional): Maximum items per page in the response. Defaults to None.
            listing_type (str | None, optional): Filter to apply (All, Local, etc.). See PieFed API docs for more info.
                Defaults to None.
            page (int | None, optional): The page number of results to request. Defaults to None.
            sort (str | None, optional): Sort method for the results (Old, New, etc.). Some sorts are only supported on
                certain type_'s. See the PieFed API docs for more info. Defaults to None.
            community_name (str | None, optional): Filter search to a specific community by name. Defaults to None.
            community_id (int | None, optional): Filter search to a specific community by id. Defaults to None.
            minimum_upvotes (int | None, optional): Filter results to only those above a certain number of upvotes.
                Defaults to None.
            nsfw (str | None, optional): How to filter NSFW results (Exclude, Include, Only). Defaults to None.

        Returns:
            dict | None: dict containing the json returned from the server. None is returned if an exception was raised
                and then subsequently ignored due to the client setting.
        """
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
        """Fetch an item from the server based on it's activitypub id.

        API endpoint: GET resolve_object

        Args:
            query (str): url of the item to resolve. If the item is not already federated to the instance, you will
                need to be authenticated.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="resolve_object", params={"q": query})

    async def federated_instances(self) -> dict | None:
        """Get lists of instances and their federation status.

        API endpoint: GET federated_instances

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="federated_instances")

    async def suggest_completion(self, query: str) -> dict | None:
        """Suggest autocompletions for users, communities, etc based on a partial string.

        API endpoint: GET suggest_completion

        Args:
            query (str): Partial username, community name, etc. Include leading character - @ for users, etc.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Fetch modlog entries.

        API endpoint: GET modlog

        Args:
            mod_person_id (int | None, optional): User id of the user doing the mod action. Defaults to None.
            community_id (int | None, optional): Community id in which action happened. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Number of items to return on the page of results. Defaults to None.
            type_ (str | None, optional): Filter by type of mod action. Defaults to None.
            other_person_id (int | None, optional): User id that mod action is directed towards. Defaults to None.
            post_id (int | None, optional): Post id of post that is being actioned. Defaults to None.
            comment_id (int | None, optional): Comment id of comment that is being actioned. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
