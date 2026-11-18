from .clients import PieFedClient, AsyncPieFedClient


class Feed:
    """Class to hold Feed endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def get(self, feed_id: int | None = None, feed_name: str | None = None) -> dict | None:
        """Get the details for a single feed.

        API endpoint: GET feed

        Args:
            feed_id (int | None, optional): Feed id of the feed being fetched. Defaults to None.
            feed_name (str | None, optional): Name of the feed to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if feed_id is not None:
            params["id"] = feed_id
        if feed_name is not None:
            params["name"] = feed_name

        return self._client.request(method="GET", endpoint="feed", params=params)

    def create(
        self,
        name: str,
        title: str,
        description: str | None = None,
        icon_url: str | None = None,
        banner_url: str | None = None,
        nsfw: bool | None = None,
        nsfl: bool | None = None,
        public: bool | None = None,
        communities: str | None = None,
        is_instance_feed: bool | None = None,
        show_child_posts: bool | None = None,
        parent_feed_id: int | None = None,
    ) -> dict | None:
        """Create a new feed.

        API endpoint: POST feed

        Args:
            name (str): url-safe name of the feed.
            title (str): Display title of the feed.
            description (str | None, optional): Sidebar content of the feed in markdown. Defaults to None.
            icon_url (str | None, optional): URL of an image to use as the feed icon. Defaults to None.
            banner_url (str | None, optional): URL of an image to use as the feed banner. Defaults to None.
            nsfw (bool | None, optional): Mark feed content as NSFW. Defaults to None.
            nsfl (bool | None, optional): Mark feed content as NSFL. Defaults to None.
            public (bool | None, optional): True if feed is public. False if private. Defaults to None.
            communities (str | None, optional): Newline-separated list of communities in the feed. Defaults to None.
            is_instance_feed (bool | None, optional): (Admins only) List feed in instance-level Explore menu. Defaults
                to None.
            show_child_posts (bool | None, optional): Show posts from children feeds in this feed. Defaults to None.
            parent_feed_id (int | None, optional): Feed id of the parent feed. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"name": name, "title": title}

        if description is not None:
            data["description"] = description
        if icon_url is not None:
            data["icon_url"] = icon_url
        if banner_url is not None:
            data["banner_url"] = banner_url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if nsfl is not None:
            data["nsfl"] = nsfl
        if public is not None:
            data["public"] = public
        if communities is not None:
            data["communities"] = communities
        if is_instance_feed is not None:
            data["is_instance_feed"] = is_instance_feed
        if show_child_posts is not None:
            data["show_child_posts"] = show_child_posts
        if parent_feed_id is not None:
            data["parent_feed_id"] = parent_feed_id

        return self._client.request(method="POST", endpoint="feed", data=data)

    def edit(
        self,
        feed_id: int,
        url: str | None = None,
        title: str | None = None,
        description: str | None = None,
        icon_url: str | None = None,
        banner_url: str | None = None,
        nsfw: bool | None = None,
        nsfl: bool | None = None,
        public: bool | None = None,
        communities: str | None = None,
        is_instance_feed: bool | None = None,
        show_child_posts: bool | None = None,
        parent_feed_id: int | None = None,
    ) -> dict | None:
        """Edit a feed.

        API endpoint: PUT feed

        Args:
            feed_id (int): Feed id of the feed being edited.
            url (str | None, optional): URL of the feed being edited. Defaults to None.
            title (str | None, optional): Display title of the feed. Defaults to None.
            description (str | None, optional): Sidebar content of the feed in markdown. Defaults to None.
            icon_url (str | None, optional): URL of an image to use as the feed icon. Set to an empty string to remove.
                Defaults to None.
            banner_url (str | None, optional): URL of an image to use as the feed banner. Set to an empty string to
                remove. Defaults to None.
            nsfw (bool | None, optional): Mark feed content as NSFW. Defaults to None.
            nsfl (bool | None, optional): Mark feed content as NSFL. Defaults to None.
            public (bool | None, optional): True if feed is public. False if private. Defaults to None.
            communities (str | None, optional): Newline-separated list of communities in the feed. Defaults to None.
            is_instance_feed (bool | None, optional): (Admins only) List feed in instance-level Explore menu. Defaults
                to None.
            show_child_posts (bool | None, optional): Show posts from children feeds in this feed. Defaults to None.
            parent_feed_id (int | None, optional): Feed id of the parent feed. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id}

        if url is not None:
            data["url"] = url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if nsfl is not None:
            data["nsfl"] = nsfl
        if public is not None:
            data["public"] = public
        if communities is not None:
            data["communities"] = communities
        if is_instance_feed is not None:
            data["is_instance_feed"] = is_instance_feed
        if show_child_posts is not None:
            data["show_child_posts"] = show_child_posts
        if parent_feed_id is not None:
            data["parent_feed_id"] = parent_feed_id

        # These fields should be deliberately included as None if passed in as an empty string
        if title is not None and title != "":
            data["title"] = title
        elif title == "":
            data["title"] = None

        if description is not None and description != "":
            data["description"] = description
        elif description == "":
            data["description"] = None

        if icon_url is not None and icon_url != "":
            data["icon_url"] = icon_url
        elif icon_url == "":
            data["icon_url"] = None

        if banner_url is not None and banner_url != "":
            data["banner_url"] = banner_url
        elif banner_url == "":
            data["banner_url"] = None

        return self._client.request(method="PUT", endpoint="feed", data=data)

    def list_feeds(self, include_communities: bool | None = None, mine_only: bool | None = None) -> dict | None:
        """Get a list of feeds.

        API endpoint: GET feed/list

        Args:
            include_communities (bool | None, optional): Include the list of communities in each feed as part of the
                response. Defaults to None.
            mine_only (bool | None, optional): Only return feeds owned by the authorized user. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if include_communities is not None:
            params["include_communities"] = include_communities
        if mine_only is not None:
            params["mine_only"] = mine_only

        return self._client.request(method="GET", endpoint="feed/list", params=params)

    def follow(self, feed_id: int, follow: bool) -> dict | None:
        """Follow or leave a feed.

        API endpoint: POST feed/follow

        Args:
            feed_id (int): Feed id of the feed being joined/left.
            follow (bool): True to join the feed. False to leave it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id, "follow": follow}

        return self._client.request(method="POST", endpoint="feed/follow", data=data)

    def delete(self, feed_id: int, deleted: bool) -> dict | None:
        """Delete or restore a feed.

        API endpoint: POST feed/delete

        Args:
            feed_id (int): Feed id of the feed being deleted/restored.
            deleted (bool): True to delete the feed. False to restore it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="feed/delete", data=data)

    def subscribe(self, feed_id: int, subscribed: bool) -> dict | None:
        """Get notifications for new posts in a feed.

        API endpoint: PUT feed/subscribe

        Args:
            feed_id (int): Feed id of the feed to receive notifications for.
            subscribed (bool): True to get notifications for a feed. False to stop.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id, "subscribe": subscribed}

        return self._client.request(method="PUT", endpoint="feed/subscribe", data=data)


class FeedAsync:
    """Class to hold async Feed endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def get(self, feed_id: int | None = None, feed_name: str | None = None) -> dict | None:
        """Get the details for a single feed.

        API endpoint: GET feed

        Args:
            feed_id (int | None, optional): Feed id of the feed being fetched. Defaults to None.
            feed_name (str | None, optional): Name of the feed to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if feed_id is not None:
            params["id"] = feed_id
        if feed_name is not None:
            params["name"] = feed_name

        return await self._client.request(method="GET", endpoint="feed", params=params)

    async def create(
        self,
        name: str,
        title: str,
        description: str | None = None,
        icon_url: str | None = None,
        banner_url: str | None = None,
        nsfw: bool | None = None,
        nsfl: bool | None = None,
        public: bool | None = None,
        communities: str | None = None,
        is_instance_feed: bool | None = None,
        show_child_posts: bool | None = None,
        parent_feed_id: int | None = None,
    ) -> dict | None:
        """Create a new feed.

        API endpoint: POST feed

        Args:
            name (str): url-safe name of the feed.
            title (str): Display title of the feed.
            description (str | None, optional): Sidebar content of the feed in markdown. Defaults to None.
            icon_url (str | None, optional): URL of an image to use as the feed icon. Defaults to None.
            banner_url (str | None, optional): URL of an image to use as the feed banner. Defaults to None.
            nsfw (bool | None, optional): Mark feed content as NSFW. Defaults to None.
            nsfl (bool | None, optional): Mark feed content as NSFL. Defaults to None.
            public (bool | None, optional): True if feed is public. False if private. Defaults to None.
            communities (str | None, optional): Newline-separated list of communities in the feed. Defaults to None.
            is_instance_feed (bool | None, optional): (Admins only) List feed in instance-level Explore menu. Defaults
                to None.
            show_child_posts (bool | None, optional): Show posts from children feeds in this feed. Defaults to None.
            parent_feed_id (int | None, optional): Feed id of the parent feed. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"name": name, "title": title}

        if description is not None:
            data["description"] = description
        if icon_url is not None:
            data["icon_url"] = icon_url
        if banner_url is not None:
            data["banner_url"] = banner_url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if nsfl is not None:
            data["nsfl"] = nsfl
        if public is not None:
            data["public"] = public
        if communities is not None:
            data["communities"] = communities
        if is_instance_feed is not None:
            data["is_instance_feed"] = is_instance_feed
        if show_child_posts is not None:
            data["show_child_posts"] = show_child_posts
        if parent_feed_id is not None:
            data["parent_feed_id"] = parent_feed_id

        return await self._client.request(method="POST", endpoint="feed", data=data)

    async def edit(
        self,
        feed_id: int,
        url: str | None = None,
        title: str | None = None,
        description: str | None = None,
        icon_url: str | None = None,
        banner_url: str | None = None,
        nsfw: bool | None = None,
        nsfl: bool | None = None,
        public: bool | None = None,
        communities: str | None = None,
        is_instance_feed: bool | None = None,
        show_child_posts: bool | None = None,
        parent_feed_id: int | None = None,
    ) -> dict | None:
        """Edit a feed.

        API endpoint: PUT feed

        Args:
            feed_id (int): Feed id of the feed being edited.
            url (str | None, optional): URL of the feed being edited. Defaults to None.
            title (str | None, optional): Display title of the feed. Defaults to None.
            description (str | None, optional): Sidebar content of the feed in markdown. Defaults to None.
            icon_url (str | None, optional): URL of an image to use as the feed icon. Set to an empty string to remove.
                Defaults to None.
            banner_url (str | None, optional): URL of an image to use as the feed banner. Set to an empty string to
                remove. Defaults to None.
            nsfw (bool | None, optional): Mark feed content as NSFW. Defaults to None.
            nsfl (bool | None, optional): Mark feed content as NSFL. Defaults to None.
            public (bool | None, optional): True if feed is public. False if private. Defaults to None.
            communities (str | None, optional): Newline-separated list of communities in the feed. Defaults to None.
            is_instance_feed (bool | None, optional): (Admins only) List feed in instance-level Explore menu. Defaults
                to None.
            show_child_posts (bool | None, optional): Show posts from children feeds in this feed. Defaults to None.
            parent_feed_id (int | None, optional): Feed id of the parent feed. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id}

        if url is not None:
            data["url"] = url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if nsfl is not None:
            data["nsfl"] = nsfl
        if public is not None:
            data["public"] = public
        if communities is not None:
            data["communities"] = communities
        if is_instance_feed is not None:
            data["is_instance_feed"] = is_instance_feed
        if show_child_posts is not None:
            data["show_child_posts"] = show_child_posts
        if parent_feed_id is not None:
            data["parent_feed_id"] = parent_feed_id

        # These fields should be deliberately included as None if passed in as an empty string
        if title is not None and title != "":
            data["title"] = title
        elif title == "":
            data["title"] = None

        if description is not None and description != "":
            data["description"] = description
        elif description == "":
            data["description"] = None

        if icon_url is not None and icon_url != "":
            data["icon_url"] = icon_url
        elif icon_url == "":
            data["icon_url"] = None

        if banner_url is not None and banner_url != "":
            data["banner_url"] = banner_url
        elif banner_url == "":
            data["banner_url"] = None

        return await self._client.request(method="PUT", endpoint="feed", data=data)

    async def list_feeds(self, include_communities: bool | None = None, mine_only: bool | None = None) -> dict | None:
        """Get a list of feeds.

        API endpoint: GET feed/list

        Args:
            include_communities (bool | None, optional): Include the list of communities in each feed as part of the
                response. Defaults to None.
            mine_only (bool | None, optional): Only return feeds owned by the authorized user. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if include_communities is not None:
            params["include_communities"] = include_communities
        if mine_only is not None:
            params["mine_only"] = mine_only

        return await self._client.request(method="GET", endpoint="feed/list", params=params)

    async def follow(self, feed_id: int, follow: bool) -> dict | None:
        """Follow or leave a feed.

        API endpoint: POST feed/follow

        Args:
            feed_id (int): Feed id of the feed being joined/left.
            follow (bool): True to join the feed. False to leave it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id, "follow": follow}

        return await self._client.request(method="POST", endpoint="feed/follow", data=data)

    async def delete(self, feed_id: int, deleted: bool) -> dict | None:
        """Delete or restore a feed.

        API endpoint: POST feed/delete

        Args:
            feed_id (int): Feed id of the feed being deleted/restored.
            deleted (bool): True to delete the feed. False to restore it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="feed/delete", data=data)

    async def subscribe(self, feed_id: int, subscribed: bool) -> dict | None:
        """Get notifications for new posts in a feed.

        API endpoint: PUT feed/subscribe

        Args:
            feed_id (int): Feed id of the feed to receive notifications for.
            subscribed (bool): True to get notifications for a feed. False to stop.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"feed_id": feed_id, "subscribe": subscribed}

        return await self._client.request(method="PUT", endpoint="feed/subscribe", data=data)
