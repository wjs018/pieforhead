from .clients import PieFedClient, AsyncPieFedClient
from .exceptions import NotImplementedError
from .utils import ExtraField


class User:
    """Class to hold User endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def get(
        self,
        person_id: int | None = None,
        username: str | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        community_id: int | None = None,
        saved_only: bool | None = None,
        include_content: bool | None = None,
    ) -> dict | None:
        """Get details for an individual user.

        API endpoint: GET user

        Args:
            person_id (int | None, optional): Get info by user id. Defaults to None.
            username (str | None, optional): Get info by username. Defaults to None.
            sort (str | None, optional): How returned content should be sorted. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.
            community_id (int | None, optional): Limit content returned to a single community. Defaults to None.
            saved_only (bool | None, optional): Only return saved content. Defaults to None.
            include_content (bool | None, optional): Should the user's content be returned. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if person_id is not None:
            params["person_id"] = person_id
        if username is not None:
            params["username"] = username
        if sort is not None:
            params["sort"] = sort
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if community_id is not None:
            params["community_id"] = community_id
        if saved_only is not None:
            params["saved_only"] = saved_only
        if include_content is not None:
            params["include_content"] = include_content

        return self._client.request(method="GET", endpoint="user", params=params)

    def get_me(self) -> dict | None:
        """Get details about the logged in user.

        API endpoint: GET user/me

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="user/me")

    def login(self, username_or_email: str, password: str) -> dict | None:
        """Log in a user.

        API endpoint: POST user/login

        Args:
            username_or_email (str): Username or email to log in with.
            password (str): Password to log in with.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.log_in(username_or_email=username_or_email, password=password, return_dict=True)

    def logout(self) -> dict | None:
        """Log out a user.

        This call is usually unnecessary and the client can just be closed instead of logging out. This can potentially
        log your account out of other devices as well.

        API endpoint: POST user/logout

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.log_out(return_dict=True)

    def block_domain(self, domain: str, block: bool) -> dict | None:
        """Add a domain block.

        API endpoint: POST domain/block

        Args:
            domain (str): Domain to block.
            block (bool): True to block. False to unblock.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        payload = {"block": block, "domain": domain}

        return self._client.request(method="POST", endpoint="domain/block", data=payload)

    def unread_count(self) -> dict | None:
        """Get the number of unread items of different types.

        API endpoint: GET user/unread_count

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="user/unread_count")

    def replies(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
        """Get the comment replies to the specific user.

        API endpoint: GET user/replies

        Args:
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            sort (str | None, optional): Sorting method for returned results. Defaults to None.
            unread_only (bool | None, optional): Only return unread results. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if unread_only is not None:
            params["unread_only"] = unread_only

        return self._client.request(method="GET", endpoint="user/replies", params=params)

    def mentions(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
        """Get the mentions of the logged in user.

        API endpoint: GET user/mentions

        Args:
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            sort (str | None, optional): Sorting method for returned content. Defaults to None.
            unread_only (bool | None, optional): Only return unread content. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if unread_only is not None:
            params["unread_only"] = unread_only

        return self._client.request(method="GET", endpoint="user/mentions", params=params)

    def media(
        self,
        limit: int | None = None,
        page: int | None = None,
    ) -> dict | None:
        """Get images uploaded by the user.

        API endpoint: GET user/media

        Args:
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page number of results to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return self._client.request(method="GET", endpoint="user/media", params=params)

    def user_block(self, person_id: int, block: bool) -> dict | None:
        """Add a user block.

        API endpoint: POST user/block

        Args:
            person_id (int): User id of the user to block.
            block (bool): True to block. False to unblock.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"block": block, "person_id": person_id}

        return self._client.request(method="POST", endpoint="user/block", data=data)

    def mark_all_as_read(self) -> dict | None:
        """Mark all notifications and messages as read.

        API endpoint: POST user/mark_all_as_read

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="POST", endpoint="user/mark_all_as_read")

    def user_subscribe(self, person_id: int, subscribe: bool) -> dict | None:
        """Get notifications for new posts by a user.

        API endpoint: PUT user/subscribe

        Args:
            person_id (int): User id to subscribe to.
            subscribe (bool): True to subscribe. False to unsubscribe.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"person_id": person_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="user/subscribe", data=data)

    def save_user_settings(
        self,
        accept_private_messages: str | None = None,
        avatar: str | None = None,
        bio: str | None = None,
        bot: bool | None = None,
        bot_visibility: str | None = None,
        reposter_visibility: str | None = None,
        community_keyword_filter: list[str] | None = None,
        cover: str | None = None,
        default_comment_sort_type: str | None = None,
        default_sort_type: str | None = None,
        display_name: str | None = None,
        email_unread: bool | None = None,
        extra_fields: list[ExtraField] | None = None,
        federate_votes: bool | None = None,
        feed_auto_follow: bool | None = None,
        feed_auto_leave: bool | None = None,
        hide_low_quality: bool | None = None,
        indexable: bool | None = None,
        newsletter: bool | None = None,
        nsfl_visibility: str | None = None,
        nsfw_visibility: str | None = None,
        genai_visibility: str | None = None,
        reply_collapse_threshold: int | None = None,
        reply_hide_threshold: int | None = None,
        show_nsfw: bool | None = None,
        show_nsfl: bool | None = None,
        show_read_posts: bool | None = None,
        searchable: bool | None = None,
        matrix_user_id: str | None = None,
    ) -> dict | None:
        """Modify user settings.

        See the PieFed API documentation for more info on possible values of each setting.

        API endpoint: PUT user/save_user_settings

        Args:
            accept_private_messages (str | None, optional): Who to accept private messages from. Defaults to None.
            avatar (str | None, optional): URL to an image to use as a user avatar. Set to an empty string to remove.
                Defaults to None.
            bio (str | None, optional): User bio in markdown. Set to an empty string to remove. Defaults to None.
            bot (bool | None, optional): Is the user a bot. Defaults to None.
            bot_visibility (str | None, optional): Visibility of bot-created posts. Defaults to None.
            reposter_visibility (str | None, optional): Visibility of reposter-created posts. Defaults to None.
            community_keyword_filter (list[str] | None, optional): List of community keywords to filter. Set to an empty
                string to remove. Defaults to None.
            cover (str | None, optional): URL to an image to use as a user banner. Set to an empty string to remove.
                Defaults to None.
            default_comment_sort_type (str | None, optional): Default sort for comments on a post. Defaults to None.
            default_sort_type (str | None, optional): Default sort type for posts. Defaults to None.
            display_name (str | None, optional): User display name. Set to an empty string to remove. Defaults to None.
            email_unread (bool | None, optional): Periodically receive emails with unread notifications. Defaults to
                None.
            extra_fields (list[ExtraField] | None, optional): Extra fields on a user's profile (max of 4). Defaults to
                None.
            federate_votes (bool | None, optional): Should votes be federated by default. Defaults to None.
            feed_auto_follow (bool | None, optional): Automatically join communities when joining a feed. Defaults to
                None.
            feed_auto_leave (bool | None, optional): Automatically unsubscribe from communities when leaving a feed.
                Defaults to None.
            hide_low_quality (bool | None, optional): Hide communities marked as low-quality. Defaults to None.
            indexable (bool | None, optional): Show up in the instance's user index. Defaults to None.
            newsletter (bool | None, optional): Receive email newsletter if an admin publishes any. Defaults to None.
            nsfl_visibility (str | None, optional): Visibility of NSFL posts. Defaults to None.
            nsfw_visibility (str | None, optional): Visibility of NSFW posts. Defaults to None.
            genai_visibility (str | None, optional): Visibility of gen-AI posts. Defaults to None.
            reply_collapse_threshold (int | None, optional): Score at which, when below, comments are collapsed.
                Defaults to None.
            reply_hide_threshold (int | None, optional): Score at which, when below, comments are hidden. Defaults to
                None.
            show_nsfw (bool | None, optional): Show NSFW posts. Defaults to None.
            show_nsfl (bool | None, optional): Show NSFL posts. Defaults to None.
            show_read_posts (bool | None, optional): Show posts marked as read. Defaults to None.
            searchable (bool | None, optional): Allow user to show up in search results. Defaults to None.
            matrix_user_id (str | None, optional): Matrix username. Set to an empty string to remove. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {}

        if accept_private_messages is not None:
            data["accept_private_messages"] = accept_private_messages
        if bot is not None:
            data["bot"] = bot
        if bot_visibility is not None:
            data["bot_visibility"] = bot_visibility
        if reposter_visibility is not None:
            data["reposter_visibility"] = reposter_visibility
        if default_comment_sort_type is not None:
            data["default_comment_sort_type"] = default_comment_sort_type
        if default_sort_type is not None:
            data["default_sort_type"] = default_sort_type
        if email_unread is not None:
            data["email_unread"] = email_unread
        if extra_fields is not None:
            data["extra_fields"] = extra_fields
        if federate_votes is not None:
            data["federate_votes"] = federate_votes
        if feed_auto_follow is not None:
            data["feed_auto_follow"] = feed_auto_follow
        if feed_auto_leave is not None:
            data["feed_auto_leave"] = feed_auto_leave
        if hide_low_quality is not None:
            data["hide_low_quality"] = hide_low_quality
        if indexable is not None:
            data["indexable"] = indexable
        if newsletter is not None:
            data["newsletter"] = newsletter
        if nsfl_visibility is not None:
            data["nsfl_visibility"] = nsfl_visibility
        if nsfw_visibility is not None:
            data["nsfw_visibility"] = nsfw_visibility
        if genai_visibility is not None:
            data["genai_visibility"] = genai_visibility
        if reply_collapse_threshold is not None:
            data["reply_collapse_threshold"] = reply_collapse_threshold
        if reply_hide_threshold is not None:
            data["reply_hide_threshold"] = reply_hide_threshold
        if show_nsfw is not None:
            data["show_nsfw"] = show_nsfw
        if show_nsfl is not None:
            data["show_nsfl"] = show_nsfl
        if show_read_posts is not None:
            data["show_read_posts"] = show_read_posts
        if searchable is not None:
            data["searchable"] = searchable

        # These parameters should be included as None if an empty string is provided
        if avatar is not None and avatar != "":
            data["avatar"] = avatar
        elif avatar == "":
            data["avatar"] = None

        if bio is not None and bio != "":
            data["bio"] = bio
        elif bio == "":
            data["bio"] = None

        if community_keyword_filter is not None and community_keyword_filter != "":
            data["community_keyword_filter"] = community_keyword_filter
        elif community_keyword_filter == "":
            data["community_keyword_filter"] = None

        if cover is not None and cover != "":
            data["cover"] = cover
        elif cover == "":
            data["cover"] = None

        if display_name is not None and display_name != "":
            data["display_name"] = display_name
        elif display_name == "":
            data["display_name"] = None

        if matrix_user_id is not None and matrix_user_id != "":
            data["matrix_user_id"] = matrix_user_id
        elif matrix_user_id == "":
            data["matrix_user_id"] = None

        return self._client.request(method="PUT", endpoint="user/save_user_settings", data=data)

    def get_notifications(
        self,
        status: str | None = None,
        limit: str | None = None,
        page: int | None = None,
    ) -> dict | None:
        """Get the notifiations for the user.

        See the PieFed API documentation for details on what notifications return what information.

        API endpoint: GET user/notifications

        Args:
            status (str | None, optional): Filter results by status. Defaults to None.
            limit (str | None, optional): Max number of results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return self._client.request(method="GET", endpoint="user/notifications", params=params)

    def mark_notification_as_read(self, notif_id: int | None, read_state: bool | None) -> dict | None:
        """Mark a notification as read.

        API endpoint: PUT user/notification_state

        Args:
            notif_id (int | None): Notification id to mark as read.
            read_state (bool | None): True to mark as read. False to mark as unread.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"notif_id": notif_id, "read_state": read_state}

        return self._client.request(method="PUT", endpoint="user/notification_state", data=data)

    def notifications_count(self) -> dict | None:
        """Get the number of unread notifications for the user.

        API endpoint: GET user/notifications_count

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="user/notifications_count")

    def mark_all_notifications_read(self) -> dict | None:
        """Mark all notifications as read.

        API endpoint: PUT user/mark_all_notifications_read

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="PUT", endpoint="user/mark_all_notifications_read")

    def verify_credentials(self, username: str, password: str) -> bool | None:
        """Verify the login credentials of the user.

        API endpoint: POST user/verify_credentials

        Args:
            username (str): Username or email.
            password (str): Password of the user.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"username": username, "password": password}

        return self._client.request(method="POST", endpoint="user/verify_credentials", data=data)

    def set_flair(self, community_id: int, flair_text: str) -> dict | None:
        """Set a user's flair in a community.

        API endpoint: POST user/set_flair

        Args:
            community_id (int): Community id that flair should show in.
            flair_text (str): Text of flair.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "flair_text": flair_text}

        return self._client.request(method="POST", endpoint="user/set_flair", data=data)

    def follow_user(self, user_id: int) -> dict | None:
        """Follow a user.

        API endpoint: POST user/follow

        Args:
            user_id (int): User id of user to follow.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"user_id": user_id}

        return self._client.request(method="POST", endpoint="user/follow", data=data)

    def unfollow_user(self, user_id: int) -> dict | None:
        """Unfollow a user.

        API endpoint: POST user/unfollow

        Args:
            user_id (int): User id of user to unfollow.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"user_id": user_id}

        return self._client.request(method="POST", endpoint="user/unfollow", data=data)

    def user_note(self, person_id: int, note: str) -> dict | None:
        """Add a note to a user.

        API endpoint: POST user/note

        Args:
            person_id (int): User id of user to mark with a note.
            note (str): Content of the note (<50 chars).

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"person_id": person_id, "note": note}

        return self._client.request(method="POST", endpoint="user/note", data=data)

    def ban_user(
        self,
        person_id: int,
        ban_ip_address: bool | None = None,
        purge_content: bool | None = None,
        reason: str | None = None,
    ) -> dict | None:
        """Ban a user.

        API endpoint: POST user/ban

        Args:
            person_id (int): User id of the user to ban.
            ban_ip_address (bool | None, optional): Also ban their IP address. Defaults to None.
            purge_content (bool | None, optional): If True, also delete all the user's content. Defaults to None.
            reason (str | None, optional): Reason for the ban. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {
            "person_id": person_id,
            "ban_ip_address": ban_ip_address,
            "purge_content": purge_content,
            "reason": reason,
        }

        return self._client.request(method="POST", endpoint="user/ban", data=data)

    def unban_user(self, person_id: int) -> dict | None:
        """Unban a user.

        API endpoint: POST user/unban

        Args:
            person_id (int): User id of the user to unban.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"person_id": person_id}

        return self._client.request(method="POST", endpoint="user/unban", data=data)

    def register(self):
        """Register a new account.

        This endpoint is unimplemented.

        API endpoint: POST user/register

        Raises:
            NotImplementedError: This enpoint is unimplemented.
        """
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    def get_captcha(self) -> dict | None:
        """Get a captcha.

        API endpoint: GET user/get_captcha

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="user/get_captcha")

    def list_activity_alerts(
        self,
        type_: str | None = None,
        filter: str | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict | None:
        """Get list of activity alerts for the user.

        API endpoint: GET user/activity_alert/list

        Args:
            type_ (str | None, optional): Only this type of item will be returned. Defaults to None.
            filter (str | None, optional): Filter by content ownership (All, Mine, Others). Defaults to None.
            sort (str | None, optional): Sorting method for returned results. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max number of items to return per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if type_ is not None:
            params["type_"] = type_
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return self._client.request(method="GET", endpoint="user/activity_alert/list", params=params)

    def activity_alert_create(
        self,
        post_id: int | None = None,
        comment_id: int | None = None,
        person_id: int | None = None,
        topic_id: int | None = None,
        feed_id: int | None = None,
        community_id: int | None = None,
    ) -> dict | None:
        """Create an activity alert.

        API endpoint: POST user/activity_alert

        Args:
            post_id (int | None, optional): Create an activity alert for a post by id. Defaults to None.
            comment_id (int | None, optional): Create an activity alert for a comment by id. Defaults to None.
            person_id (int | None, optional): Create an activity alert for a user by id. Defaults to None.
            topic_id (int | None, optional): Create an activity alert for a topic by id. Defaults to None.
            feed_id (int | None, optional): Create an activity alert for a feed by id. Defaults to None.
            community_id (int | None, optional): Create an activity alert for a community by it. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {}

        if post_id is not None:
            data["post_id"] = post_id
        if comment_id is not None:
            data["comment_id"] = comment_id
        if person_id is not None:
            data["person_id"] = person_id
        if topic_id is not None:
            data["topic_id"] = topic_id
        if feed_id is not None:
            data["feed_id"] = feed_id
        if community_id is not None:
            data["community_id"] = community_id

        return self._client.request(method="POST", endpoint="user/activity_alert", data=data)

    def activity_alert_delete(
        self,
        post_id: int | None = None,
        comment_id: int | None = None,
        person_id: int | None = None,
        topic_id: int | None = None,
        feed_id: int | None = None,
        community_id: int | None = None,
    ) -> dict | None:
        """Delete an activity alert.

        API endpoint: POST user/activity_alert/delete

        Args:
            post_id (int | None, optional): Remove an activity alert on a post. Defaults to None.
            comment_id (int | None, optional): Remove an activity alert on a comment. Defaults to None.
            person_id (int | None, optional): Remove an activity alert on a user. Defaults to None.
            topic_id (int | None, optional): Remove an activity alert on a topic. Defaults to None.
            feed_id (int | None, optional): Remove an activity alert on a feed. Defaults to None.
            community_id (int | None, optional): Remove an activity alert on a community. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {}

        if post_id is not None:
            data["post_id"] = post_id
        if comment_id is not None:
            data["comment_id"] = comment_id
        if person_id is not None:
            data["person_id"] = person_id
        if topic_id is not None:
            data["topic_id"] = topic_id
        if feed_id is not None:
            data["feed_id"] = feed_id
        if community_id is not None:
            data["community_id"] = community_id

        return self._client.request(method="POST", endpoint="user/activity_alert/delete", data=data)


class UserAsync:
    """Class to hold async User endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def get(
        self,
        person_id: int | None = None,
        username: str | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        community_id: int | None = None,
        saved_only: bool | None = None,
        include_content: bool | None = None,
    ) -> dict | None:
        """Get details for an individual user.

        API endpoint: GET user

        Args:
            person_id (int | None, optional): Get info by user id. Defaults to None.
            username (str | None, optional): Get info by username. Defaults to None.
            sort (str | None, optional): How returned content should be sorted. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.
            community_id (int | None, optional): Limit content returned to a single community. Defaults to None.
            saved_only (bool | None, optional): Only return saved content. Defaults to None.
            include_content (bool | None, optional): Should the user's content be returned. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if person_id is not None:
            params["person_id"] = person_id
        if username is not None:
            params["username"] = username
        if sort is not None:
            params["sort"] = sort
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if community_id is not None:
            params["community_id"] = community_id
        if saved_only is not None:
            params["saved_only"] = saved_only
        if include_content is not None:
            params["include_content"] = include_content

        return await self._client.request(method="GET", endpoint="user", params=params)

    async def get_me(self) -> dict | None:
        """Get details about the logged in user.

        API endpoint: GET user/me

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="user/me")

    async def login(self, username_or_email: str, password: str) -> dict | None:
        """Log in a user.

        API endpoint: POST user/login

        Args:
            username_or_email (str): Username or email to log in with.
            password (str): Password to log in with.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.log_in(
            username_or_email=username_or_email,
            password=password,
            return_dict=True,
        )

    async def logout(self) -> dict | None:
        """Log out a user.

        This call is usually unnecessary and the client can just be closed instead of logging out. This can potentially
        log your account out of other devices as well.

        API endpoint: POST user/logout

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.log_out(return_dict=True)

    async def block_domain(self, domain: str, block: bool) -> dict | None:
        """Add a domain block.

        API endpoint: POST domain/block

        Args:
            domain (str): Domain to block.
            block (bool): True to block. False to unblock.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        payload = {"block": block, "domain": domain}

        return await self._client.request(method="POST", endpoint="domain/block", data=payload)

    async def unread_count(self) -> dict | None:
        """Get the number of unread items of different types.

        API endpoint: GET user/unread_count

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="user/unread_count")

    async def replies(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
        """Get the comment replies to the specific user.

        API endpoint: GET user/replies

        Args:
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            sort (str | None, optional): Sorting method for returned results. Defaults to None.
            unread_only (bool | None, optional): Only return unread results. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if unread_only is not None:
            params["unread_only"] = unread_only

        return await self._client.request(method="GET", endpoint="user/replies", params=params)

    async def mentions(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
        """Get the mentions of the logged in user.

        API endpoint: GET user/mentions

        Args:
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            sort (str | None, optional): Sorting method for returned content. Defaults to None.
            unread_only (bool | None, optional): Only return unread content. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if unread_only is not None:
            params["unread_only"] = unread_only

        return await self._client.request(method="GET", endpoint="user/mentions", params=params)

    async def media(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
        """Get images uploaded by the user.

        API endpoint: GET user/media

        Args:
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page number of results to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if unread_only is not None:
            params["unread_only"] = unread_only

        return await self._client.request(method="GET", endpoint="user/media", params=params)

    async def user_block(self, person_id: int, block: bool) -> dict | None:
        """Add a user block.

        API endpoint: POST user/block

        Args:
            person_id (int): User id of the user to block.
            block (bool): True to block. False to unblock.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"block": block, "person_id": person_id}

        return await self._client.request(method="POST", endpoint="user/block", data=data)

    async def mark_all_as_read(self) -> dict | None:
        """Mark all notifications and messages as read.

        API endpoint: POST user/mark_all_as_read

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="POST", endpoint="user/mark_all_as_read")

    async def user_subscribe(self, person_id: int, subscribe: bool) -> dict | None:
        """Get notifications for new posts by a user.

        API endpoint: PUT user/subscribe

        Args:
            person_id (int): User id to subscribe to.
            subscribe (bool): True to subscribe. False to unsubscribe.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"person_id": person_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="user/subscribe", data=data)

    async def save_user_settings(
        self,
        accept_private_messages: str | None = None,
        avatar: str | None = None,
        bio: str | None = None,
        bot: bool | None = None,
        bot_visibility: str | None = None,
        reposter_visibility: str | None = None,
        community_keyword_filter: list[str] | None = None,
        cover: str | None = None,
        default_comment_sort_type: str | None = None,
        default_sort_type: str | None = None,
        display_name: str | None = None,
        email_unread: bool | None = None,
        extra_fields: list[ExtraField] | None = None,
        federate_votes: bool | None = None,
        feed_auto_follow: bool | None = None,
        feed_auto_leave: bool | None = None,
        hide_low_quality: bool | None = None,
        indexable: bool | None = None,
        newsletter: bool | None = None,
        nsfl_visibility: str | None = None,
        nsfw_visibility: str | None = None,
        genai_visibility: str | None = None,
        reply_collapse_threshold: int | None = None,
        reply_hide_threshold: int | None = None,
        show_nsfw: bool | None = None,
        show_nsfl: bool | None = None,
        show_read_posts: bool | None = None,
        searchable: bool | None = None,
        matrix_user_id: str | None = None,
    ) -> dict | None:
        """Modify user settings.

        See the PieFed API documentation for more info on possible values of each setting.

        API endpoint: PUT user/save_user_settings

        Args:
            accept_private_messages (str | None, optional): Who to accept private messages from. Defaults to None.
            avatar (str | None, optional): URL to an image to use as a user avatar. Set to an empty string to remove.
                Defaults to None.
            bio (str | None, optional): User bio in markdown. Set to an empty string to remove. Defaults to None.
            bot (bool | None, optional): Is the user a bot. Defaults to None.
            bot_visibility (str | None, optional): Visibility of bot-created posts. Defaults to None.
            reposter_visibility (str | None, optional): Visibility of reposter-created posts. Defaults to None.
            community_keyword_filter (list[str] | None, optional): List of community keywords to filter. Set to an empty
                string to remove. Defaults to None.
            cover (str | None, optional): URL to an image to use as a user banner. Set to an empty string to remove.
                Defaults to None.
            default_comment_sort_type (str | None, optional): Default sort for comments on a post. Defaults to None.
            default_sort_type (str | None, optional): Default sort type for posts. Defaults to None.
            display_name (str | None, optional): User display name. Set to an empty string to remove. Defaults to None.
            email_unread (bool | None, optional): Periodically receive emails with unread notifications. Defaults to
                None.
            extra_fields (list[ExtraField] | None, optional): Extra fields on a user's profile (max of 4). Defaults to
                None.
            federate_votes (bool | None, optional): Should votes be federated by default. Defaults to None.
            feed_auto_follow (bool | None, optional): Automatically join communities when joining a feed. Defaults to
                None.
            feed_auto_leave (bool | None, optional): Automatically unsubscribe from communities when leaving a feed.
                Defaults to None.
            hide_low_quality (bool | None, optional): Hide communities marked as low-quality. Defaults to None.
            indexable (bool | None, optional): Show up in the instance's user index. Defaults to None.
            newsletter (bool | None, optional): Receive email newsletter if an admin publishes any. Defaults to None.
            nsfl_visibility (str | None, optional): Visibility of NSFL posts. Defaults to None.
            nsfw_visibility (str | None, optional): Visibility of NSFW posts. Defaults to None.
            genai_visibility (str | None, optional): Visibility of gen-AI posts. Defaults to None.
            reply_collapse_threshold (int | None, optional): Score at which, when below, comments are collapsed.
                Defaults to None.
            reply_hide_threshold (int | None, optional): Score at which, when below, comments are hidden. Defaults to
                None.
            show_nsfw (bool | None, optional): Show NSFW posts. Defaults to None.
            show_nsfl (bool | None, optional): Show NSFL posts. Defaults to None.
            show_read_posts (bool | None, optional): Show posts marked as read. Defaults to None.
            searchable (bool | None, optional): Allow user to show up in search results. Defaults to None.
            matrix_user_id (str | None, optional): Matrix username. Set to an empty string to remove. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {}

        if accept_private_messages is not None:
            data["accept_private_messages"] = accept_private_messages
        if bot is not None:
            data["bot"] = bot
        if bot_visibility is not None:
            data["bot_visibility"] = bot_visibility
        if reposter_visibility is not None:
            data["reposter_visibility"] = reposter_visibility
        if default_comment_sort_type is not None:
            data["default_comment_sort_type"] = default_comment_sort_type
        if default_sort_type is not None:
            data["default_sort_type"] = default_sort_type
        if email_unread is not None:
            data["email_unread"] = email_unread
        if extra_fields is not None:
            data["extra_fields"] = extra_fields
        if federate_votes is not None:
            data["federate_votes"] = federate_votes
        if feed_auto_follow is not None:
            data["feed_auto_follow"] = feed_auto_follow
        if feed_auto_leave is not None:
            data["feed_auto_leave"] = feed_auto_leave
        if hide_low_quality is not None:
            data["hide_low_quality"] = hide_low_quality
        if indexable is not None:
            data["indexable"] = indexable
        if newsletter is not None:
            data["newsletter"] = newsletter
        if nsfl_visibility is not None:
            data["nsfl_visibility"] = nsfl_visibility
        if nsfw_visibility is not None:
            data["nsfw_visibility"] = nsfw_visibility
        if genai_visibility is not None:
            data["genai_visibility"] = genai_visibility
        if reply_collapse_threshold is not None:
            data["reply_collapse_threshold"] = reply_collapse_threshold
        if reply_hide_threshold is not None:
            data["reply_hide_threshold"] = reply_hide_threshold
        if show_nsfw is not None:
            data["show_nsfw"] = show_nsfw
        if show_nsfl is not None:
            data["show_nsfl"] = show_nsfl
        if show_read_posts is not None:
            data["show_read_posts"] = show_read_posts
        if searchable is not None:
            data["searchable"] = searchable

        if avatar is not None and avatar != "":
            data["avatar"] = avatar
        elif avatar == "":
            data["avatar"] = None

        if bio is not None and bio != "":
            data["bio"] = bio
        elif bio == "":
            data["bio"] = None

        if community_keyword_filter is not None and community_keyword_filter != "":
            data["community_keyword_filter"] = community_keyword_filter
        elif community_keyword_filter == "":
            data["community_keyword_filter"] = None

        if cover is not None and cover != "":
            data["cover"] = cover
        elif cover == "":
            data["cover"] = None

        if display_name is not None and display_name != "":
            data["display_name"] = display_name
        elif display_name == "":
            data["display_name"] = None

        if matrix_user_id is not None and matrix_user_id != "":
            data["matrix_user_id"] = matrix_user_id
        elif matrix_user_id == "":
            data["matrix_user_id"] = None

        return await self._client.request(method="PUT", endpoint="user/save_user_settings", data=data)

    async def get_notifications(
        self,
        status: str | None = None,
        limit: str | None = None,
        page: int | None = None,
    ) -> dict | None:
        """Get the notifiations for the user.

        See the PieFed API documentation for details on what notifications return what information.

        API endpoint: GET user/notifications

        Args:
            status (str | None, optional): Filter results by status. Defaults to None.
            limit (str | None, optional): Max number of results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return await self._client.request(method="GET", endpoint="user/notifications", params=params)

    async def mark_notification_as_read(self, notif_id: int | None, read_state: bool | None) -> dict | None:
        """Mark a notification as read.

        API endpoint: PUT user/notification_state

        Args:
            notif_id (int | None): Notification id to mark as read.
            read_state (bool | None): True to mark as read. False to mark as unread.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"notif_id": notif_id, "read_state": read_state}

        return await self._client.request(method="PUT", endpoint="user/notification_state", data=data)

    async def notifications_count(self) -> dict | None:
        """Get the number of unread notifications for the user.

        API endpoint: GET user/notifications_count

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="user/notifications_count")

    async def mark_all_notifications_read(self) -> dict | None:
        """Mark all notifications as read.

        API endpoint: PUT user/mark_all_notifications_read

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="PUT", endpoint="user/mark_all_notifications_read")

    async def verify_credentials(self, username: str, password: str) -> bool | None:
        """Verify the login credentials of the user.

        API endpoint: POST user/verify_credentials

        Args:
            username (str): Username or email.
            password (str): Password of the user.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"username": username, "password": password}

        return await self._client.request(method="POST", endpoint="user/verify_credentials", data=data)

    async def set_flair(self, community_id: int, flair_text: str) -> dict | None:
        """Set a user's flair in a community.

        API endpoint: POST user/set_flair

        Args:
            community_id (int): Community id that flair should show in.
            flair_text (str): Text of flair.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "flair_text": flair_text}

        return await self._client.request(method="POST", endpoint="user/set_flair", data=data)

    async def follow_user(self, user_id: int) -> dict | None:
        """Follow a user.

        API endpoint: POST user/follow

        Args:
            user_id (int): User id of user to follow.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"user_id": user_id}

        return await self._client.request(method="POST", endpoint="user/follow", data=data)

    async def unfollow_user(self, user_id: int) -> dict | None:
        """Unfollow a user.

        API endpoint: POST user/unfollow

        Args:
            user_id (int): User id of user to unfollow.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"user_id": user_id}

        return await self._client.request(method="POST", endpoint="user/unfollow", data=data)

    async def user_note(self, person_id: int, note: str) -> dict | None:
        """Add a note to a user.

        API endpoint: POST user/note

        Args:
            person_id (int): User id of user to mark with a note.
            note (str): Content of the note (<50 chars).

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"person_id": person_id, "note": note}

        return await self._client.request(method="POST", endpoint="user/note", data=data)

    async def ban_user(
        self,
        person_id: int,
        ban_ip_address: bool | None = None,
        purge_content: bool | None = None,
        reason: str | None = None,
    ) -> dict | None:
        """Ban a user.

        API endpoint: POST user/ban

        Args:
            person_id (int): User id of the user to ban.
            ban_ip_address (bool | None, optional): Also ban their IP address. Defaults to None.
            purge_content (bool | None, optional): If True, also delete all the user's content. Defaults to None.
            reason (str | None, optional): Reason for the ban. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {
            "person_id": person_id,
            "ban_ip_address": ban_ip_address,
            "purge_content": purge_content,
            "reason": reason,
        }

        return await self._client.request(method="POST", endpoint="user/ban", data=data)

    async def unban_user(self, person_id: int) -> dict | None:
        """Unban a user.

        API endpoint: POST user/unban

        Args:
            person_id (int): User id of the user to unban.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"person_id": person_id}

        return await self._client.request(method="POST", endpoint="user/unban", data=data)

    async def list_activity_alerts(
        self,
        type_: str | None = None,
        filter: str | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict | None:
        """Get list of activity alerts for the user.

        API endpoint: GET user/activity_alert/list

        Args:
            type_ (str | None, optional): Only this type of item will be returned. Defaults to None.
            filter (str | None, optional): Filter by content ownership (All, Mine, Others). Defaults to None.
            sort (str | None, optional): Sorting method for returned results. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max number of items to return per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if type_ is not None:
            params["type_"] = type_
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="user/activity_alert/list", params=params)

    async def activity_alert_create(
        self,
        post_id: int | None = None,
        comment_id: int | None = None,
        person_id: int | None = None,
        topic_id: int | None = None,
        feed_id: int | None = None,
        community_id: int | None = None,
    ) -> dict | None:
        """Create an activity alert.

        API endpoint: POST user/activity_alert

        Args:
            post_id (int | None, optional): Create an activity alert for a post by id. Defaults to None.
            comment_id (int | None, optional): Create an activity alert for a comment by id. Defaults to None.
            person_id (int | None, optional): Create an activity alert for a user by id. Defaults to None.
            topic_id (int | None, optional): Create an activity alert for a topic by id. Defaults to None.
            feed_id (int | None, optional): Create an activity alert for a feed by id. Defaults to None.
            community_id (int | None, optional): Create an activity alert for a community by it. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {}

        if post_id is not None:
            data["post_id"] = post_id
        if comment_id is not None:
            data["comment_id"] = comment_id
        if person_id is not None:
            data["person_id"] = person_id
        if topic_id is not None:
            data["topic_id"] = topic_id
        if feed_id is not None:
            data["feed_id"] = feed_id
        if community_id is not None:
            data["community_id"] = community_id

        return await self._client.request(method="POST", endpoint="user/activity_alert", data=data)

    async def activity_alert_delete(
        self,
        post_id: int | None = None,
        comment_id: int | None = None,
        person_id: int | None = None,
        topic_id: int | None = None,
        feed_id: int | None = None,
        community_id: int | None = None,
    ) -> dict | None:
        """Delete an activity alert.

        API endpoint: POST user/activity_alert/delete

        Args:
            post_id (int | None, optional): Remove an activity alert on a post. Defaults to None.
            comment_id (int | None, optional): Remove an activity alert on a comment. Defaults to None.
            person_id (int | None, optional): Remove an activity alert on a user. Defaults to None.
            topic_id (int | None, optional): Remove an activity alert on a topic. Defaults to None.
            feed_id (int | None, optional): Remove an activity alert on a feed. Defaults to None.
            community_id (int | None, optional): Remove an activity alert on a community. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {}

        if post_id is not None:
            data["post_id"] = post_id
        if comment_id is not None:
            data["comment_id"] = comment_id
        if person_id is not None:
            data["person_id"] = person_id
        if topic_id is not None:
            data["topic_id"] = topic_id
        if feed_id is not None:
            data["feed_id"] = feed_id
        if community_id is not None:
            data["community_id"] = community_id

        return await self._client.request(method="POST", endpoint="user/activity_alert/delete", data=data)

    async def register(self):
        """Register a new account.

        This endpoint is unimplemented.

        API endpoint: POST user/register

        Raises:
            NotImplementedError: This enpoint is unimplemented.
        """
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    async def get_captcha(self):
        """Get a captcha.

        API endpoint: GET user/get_captcha

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="user/get_captcha")
