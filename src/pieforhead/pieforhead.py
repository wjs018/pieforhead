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
from .private_message import PrivateMessage, PrivateMessageAsync
from .community import Community, CommunityAsync
from .post import Post, PostAsync
from .comment import Comment, CommentAsync

logger = logging.getLogger(__name__)


class PieFed:
    """Class for accessing synchronous client."""

    _client: PieFedClient

    def __init__(self, instance_url: str, timeout: float = 5.0, raise_exceptions: bool = True):
        """Creates a PieFedClient for the given instance.

        Args:
            instance_url (str): URL of the instance to connect to, e.g. https://instance.tld/
            timeout (float, optional): Seconds to wait before timing out on requests. Defaults to 5.0.
            raise_exceptions (bool, optional): Should failed requests raise an exception or just return None. Defaults
                to True.
        """
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
        self.private_message = PrivateMessage(client=self._client)
        self.community = Community(client=self._client)
        self.post = Post(client=self._client)
        self.comment = Comment(client=self._client)

    def __enter__(self):
        return self

    def login(self, username_or_email: str, password: str) -> bool:
        """Log into an instance.

        Identical to the log_in function.

        API endpoint: POST user/login

        Args:
            username_or_email (str): Username or email to log in with (case-insensitive).
            password (str): Password for authentication.

        Returns:
            bool: Returns True if login was successful.
        """
        return self.log_in(username_or_email, password)

    def log_in(self, username_or_email: str, password: str) -> bool:
        """Log into an instance.

        Identical to the login function.

        API endpoint: POST user/login

        Args:
            username_or_email (str): Username or email to log in with (case-insensitive).
            password (str): Password for authentication.

        Returns:
            bool: Returns True if login was successful.
        """
        return self._client.log_in(username_or_email, password)

    def is_logged_in(self) -> bool:
        """Verify that the client has login credentials.

        Returns:
            bool: True is login credentials are saved in the client.
        """
        return self._client.is_logged_in()

    def log_out(self) -> bool:
        """Logs out of the instance and invalidates auth token.

        This call is usually unnecessary and the client can just be closed instead of logging out. This can potentially
        log your account out of other devices as well.

        API endpoint: POST user/logout

        Returns:
            bool: Returns true if logout was successful.
        """
        return self._client.log_out()

    def close(self):
        """Closes the client and any remaining connection that might be open."""
        self._client.close()

    def __exit__(self, *args):
        self.close()

    @property
    def instance_version(self) -> semver.Version:
        """Get the PieFed version of the instance.

        Returns:
            semver.Version: PieFed software version.
        """
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
        """Fetch an item from the server based on it's activitypub id.

        API endpoint: GET resolve_object

        Args:
            query (str): url of the item to resolve. If the item is not already federated to the instance, you will
                need to be authenticated.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self.misc.resolve_object(query=query)

    def federated_instances(self) -> dict | None:
        """Get lists of instances and their federation status.

        API endpoint: GET federated_instances

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self.misc.federated_instances()

    def suggest_completion(self, query: str) -> dict | None:
        """Suggest autocompletions for users, communities, etc based on a partial string.

        API endpoint: GET suggest_completion

        Args:
            query (str): Partial username, community name, etc. Include leading character - @ for users, etc.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
    """Class for accessing the asynchronous client."""

    _client: AsyncPieFedClient
    instance_url: str

    def __init__(self, instance_url: str, timeout: float = 5.0, raise_exceptions: bool = True):
        """Creates an AsyncPieFedClient for the given instance.

        Args:
            instance_url (str): URL of the instance to connect to, e.g. https://instance.tld/
            timeout (float, optional): Seconds to wait before timing out on requests. Defaults to 5.0.
            raise_exceptions (bool, optional): Should failed requests raise an exception or just return None. Defaults
                to True.
        """
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
        self.private_message = PrivateMessageAsync(client=self._client)
        self.community = CommunityAsync(client=self._client)
        self.post = PostAsync(client=self._client)
        self.comment = CommentAsync(client=self._client)

    async def __aenter__(self):
        return self

    async def login(self, username_or_email: str, password: str) -> bool:
        """Log into an instance.

        Identical to the log_in function.

        API endpoint: POST user/login

        Args:
            username_or_email (str): Username or email to log in with (case-insensitive).
            password (str): Password for authentication.

        Returns:
            bool: Returns True if login was successful.
        """
        return self.log_in(username_or_email, password)

    async def log_in(self, username_or_email: str, password: str) -> bool:
        """Log into an instance.

        Identical to the login function.

        API endpoint: POST user/login

        Args:
            username_or_email (str): Username or email to log in with (case-insensitive).
            password (str): Password for authentication.

        Returns:
            bool: Returns True if login was successful.
        """
        return await self._client.log_in(username_or_email, password)

    async def is_logged_in(self) -> bool:
        """Verify that the client has login credentials.

        Returns:
            bool: True is login credentials are saved in the client.
        """
        return await self._client.is_logged_in()

    async def log_out(self) -> bool:
        """Logs out of the instance and invalidates auth token.

        This call is usually unnecessary and the client can just be closed instead of logging out. This can potentially
        log your account out of other devices as well.

        API endpoint: POST user/logout

        Returns:
            bool: Returns true if logout was successful.
        """
        return await self._client.log_out()

    async def close(self):
        """Closes the client and any remaining connection that might be open."""
        await self._client.close()

    async def __aexit__(self, *args):
        await self.close()

    @property
    async def instance_version(self) -> semver.Version:
        """Get the PieFed version of the instance.

        Returns:
            semver.Version: PieFed software version.
        """
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
        """Fetch an item from the server based on it's activitypub id.

        API endpoint: GET resolve_object

        Args:
            query (str): url of the item to resolve. If the item is not already federated to the instance, you will
                need to be authenticated.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self.misc.resolve_object(query=query)

    async def federated_instances(self) -> dict | None:
        """Get lists of instances and their federation status.

        API endpoint: GET federated_instances

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self.misc.federated_instances()

    async def suggest_completion(self, query: str) -> dict | None:
        """Suggest autocompletions for users, communities, etc based on a partial string.

        API endpoint: GET suggest_completion

        Args:
            query (str): Partial username, community name, etc. Include leading character - @ for users, etc.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
