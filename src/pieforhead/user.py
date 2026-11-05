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
        return self._client.request(method="GET", endpoint="user/me")

    def login(self, username_or_email: str, password: str) -> dict | None:
        return self._client.log_in(username_or_email=username_or_email, password=password, return_dict=True)

    def logout(self) -> dict | None:
        return self._client.log_out(return_dict=True)

    def block_domain(self, domain: str, block: bool) -> dict | None:
        payload = {"block": block, "domain": domain}

        return self._client.request(method="POST", endpoint="domain/block", data=payload)

    def unread_count(self) -> dict | None:
        return self._client.request(method="GET", endpoint="user/unread_count")

    def replies(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
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
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if unread_only is not None:
            params["unread_only"] = unread_only

        return self._client.request(method="GET", endpoint="user/media", params=params)

    def user_block(self, person_id: int, block: bool) -> dict | None:
        data = {"block": block, "person_id": person_id}

        return self._client.request(method="POST", endpoint="user/block", data=data)

    def mark_all_as_read(self) -> dict | None:
        return self._client.request(method="POST", endpoint="user/mark_all_as_read")

    def user_subscribe(self, person_id: int, subscribe: bool) -> dict | None:
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
        params = {}

        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return self._client.request(method="GET", endpoint="user/notifications", params=params)

    def mark_notification_as_read(self, notif_id: int | None, read_state: bool | None) -> dict | None:
        data = {"notif_id": notif_id, "read_state": read_state}

        return self._client.request(method="PUT", endpoint="user/notification_state", data=data)

    def notifications_count(self) -> dict | None:
        return self._client.request(method="GET", endpoint="user/notifications_count")

    def mark_all_notifications_read(self) -> dict | None:
        return self._client.request(method="PUT", endpoint="user/mark_all_notifications_read")

    def verify_credentials(self, username: str, password: str) -> bool | None:
        data = {"username": username, "password": password}

        return self._client.request(method="POST", endpoint="user/verify_credentials", data=data)

    def set_flair(self, community_id: int, flair_text: str) -> dict | None:
        data = {"community_id": community_id, "flair_text": flair_text}

        return self._client.request(method="POST", endpoint="user/set_flair", data=data)

    def follow_user(self, user_id: int) -> dict | None:
        data = {"user_id": user_id}

        return self._client.request(method="POST", endpoint="user/follow", data=data)

    def unfollow_user(self, user_id: int) -> dict | None:
        data = {"user_id": user_id}

        return self._client.request(method="POST", endpoint="user/unfollow", data=data)

    def user_note(self, person_id: int, note: str) -> dict | None:
        data = {"person_id": person_id, "note": note}

        return self._client.request(method="POST", endpoint="user/note", data=data)

    def ban_user(
        self,
        person_id: int,
        ban_ip_address: bool | None = None,
        purge_content: bool | None = None,
        reason: str | None = None,
    ) -> dict | None:
        data = {
            "person_id": person_id,
            "ban_ip_address": ban_ip_address,
            "purge_content": purge_content,
            "reason": reason,
        }

        return self._client.request(method="POST", endpoint="user/ban", data=data)

    def unban_user(self, person_id: int) -> dict | None:
        data = {"person_id": person_id}

        return self._client.request(method="POST", endpoint="user/unban", data=data)

    def register(self):
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    def get_captcha(self) -> dict | None:
        return self._client.request(method="GET", endpoint="user/get_captcha")

    def list_activity_alerts(
        self,
        type_: str | None = None,
        filter: str | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict | None:
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
        return await self._client.request(method="GET", endpoint="user/me")

    async def login(self, username_or_email: str, password: str) -> dict | None:
        return await self._client.log_in(
            username_or_email=username_or_email,
            password=password,
            return_dict=True,
        )

    async def logout(self) -> dict | None:
        return await self._client.log_out(return_dict=True)

    async def block_domain(self, domain: str, block: bool) -> dict | None:
        payload = {"block": block, "domain": domain}

        return await self._client.request(method="POST", endpoint="domain/block", data=payload)

    async def unread_count(self) -> dict | None:
        return await self._client.request(method="GET", endpoint="user/unread_count")

    async def replies(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
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
        data = {"block": block, "person_id": person_id}

        return await self._client.request(method="POST", endpoint="user/block", data=data)

    async def mark_all_as_read(self) -> dict | None:
        return await self._client.request(method="POST", endpoint="user/mark_all_as_read")

    async def user_subscribe(self, person_id: int, subscribe: bool) -> dict | None:
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
        params = {}

        if status is not None:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return await self._client.request(method="GET", endpoint="user/notifications", params=params)

    async def mark_notification_as_read(self, notif_id: int | None, read_state: bool | None) -> dict | None:
        data = {"notif_id": notif_id, "read_state": read_state}

        return await self._client.request(method="PUT", endpoint="user/notification_state", data=data)

    async def notifications_count(self) -> dict | None:
        return await self._client.request(method="GET", endpoint="user/notifications_count")

    async def mark_all_notifications_read(self) -> dict | None:
        return await self._client.request(method="PUT", endpoint="user/mark_all_notifications_read")

    async def verify_credentials(self, username: str, password: str) -> bool | None:
        data = {"username": username, "password": password}

        return await self._client.request(method="POST", endpoint="user/verify_credentials", data=data)

    async def set_flair(self, community_id: int, flair_text: str) -> dict | None:
        data = {"community_id": community_id, "flair_text": flair_text}

        return await self._client.request(method="POST", endpoint="user/set_flair", data=data)

    async def follow_user(self, user_id: int) -> dict | None:
        data = {"user_id": user_id}

        return await self._client.request(method="POST", endpoint="user/follow", data=data)

    async def unfollow_user(self, user_id: int) -> dict | None:
        data = {"user_id": user_id}

        return await self._client.request(method="POST", endpoint="user/unfollow", data=data)

    async def user_note(self, person_id: int, note: str) -> dict | None:
        data = {"person_id": person_id, "note": note}

        return await self._client.request(method="POST", endpoint="user/note", data=data)

    async def ban_user(
        self,
        person_id: int,
        ban_ip_address: bool | None = None,
        purge_content: bool | None = None,
        reason: str | None = None,
    ) -> dict | None:
        data = {
            "person_id": person_id,
            "ban_ip_address": ban_ip_address,
            "purge_content": purge_content,
            "reason": reason,
        }

        return await self._client.request(method="POST", endpoint="user/ban", data=data)

    async def unban_user(self, person_id: int) -> dict | None:
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
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    async def get_captcha(self):
        return await self._client.request(method="GET", endpoint="user/get_captcha")
