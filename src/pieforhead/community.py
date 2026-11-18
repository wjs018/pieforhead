from .clients import PieFedClient, AsyncPieFedClient


class Community:
    """Class to hold Community endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def get(self, community_id: int | None = None, name: str | None = None) -> dict | None:
        """Get details for a single community.

        API endpoint: GET community

        Args:
            community_id (int | None, optional): Community id of the community to fetch. Defaults to None.
            name (str | None, optional): Name of the community to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if community_id is not None:
            params["id"] = community_id
        if name is not None:
            params["name"] = name

        return self._client.request(method="GET", endpoint="community", params=params)

    def create(
        self,
        name: str,
        title: str,
        banner_url: str | None = None,
        description: str | None = None,
        discussion_languages: list[int] | None = None,
        icon_url: str | None = None,
        local_only: bool | None = None,
        nsfw: bool | None = None,
        question_answer: bool | None = None,
        restricted_to_mods: bool | None = None,
        rules: str | None = None,
    ) -> dict | None:
        """Create a new community.

        API endpoint: POST community

        Args:
            name (str): Name of the community (part of url, so needs to be url-safe)
            title (str): Displayed title of the community.
            banner_url (str | None, optional): URL of image to use as community banner. Defaults to None.
            description (str | None, optional): Sidebar contents of the community in markdown. Defaults to None.
            discussion_languages (list[int] | None, optional): Allowed language ids for the community. Defaults to None.
            icon_url (str | None, optional): URL of image to use as community icon. Defaults to None.
            local_only (bool | None, optional): Make this community local-only. Defaults to None.
            nsfw (bool | None, optional): Make community entirely NSFW or not. Defaults to None.
            question_answer (bool | None, optional): Make community a question and answer community. Defaults to None.
            restricted_to_mods (bool | None, optional): Only allow posts by moderators. Defaults to None.
            rules (str | None, optional): Rules field for the community. This field is deprecated. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"name": name, "title": title}

        if description is not None:
            data["description"] = description
        if discussion_languages is not None:
            data["discussion_languages"] = discussion_languages
        if local_only is not None:
            data["local_only"] = local_only
        if nsfw is not None:
            data["nsfw"] = nsfw
        if question_answer is not None:
            data["question_answer"] = question_answer
        if restricted_to_mods is not None:
            data["restricted_to_mods"] = restricted_to_mods
        if rules is not None:
            data["rules"] = rules

        if banner_url is not None and banner_url != "":
            data["banner_url"] = banner_url
        elif banner_url == "":
            data["banner_url"] = None

        if icon_url is not None and icon_url != "":
            data["icon_url"] = icon_url
        elif icon_url == "":
            data["icon_url"] = None

        return self._client.request(method="POST", endpoint="community", data=data)

    def edit(
        self,
        community_id: int,
        title: str | None = None,
        banner_url: str | None = None,
        description: str | None = None,
        discussion_languages: list[int] | None = None,
        icon_url: str | None = None,
        local_only: bool | None = None,
        nsfw: bool | None = None,
        restricted_to_mods: bool | None = None,
        question_answer: bool | None = None,
        rules: str | None = None,
    ) -> dict | None:
        """Edit a community.

        API endpoint: PUT community

        Args:
            community_id (int): Community id of the community to edit.
            title (str | None, optional): Display title of the community. Set to an empty string to remove.
                Defaults to None.
            banner_url (str | None, optional): URL of image to use as community banner. Set to an empty string to
                remove. Defaults to None.
            description (str | None, optional): Sidebar contents of the community. Set to an empty string to remove.
                Defaults to None.
            discussion_languages (list[int] | None, optional): Allowed language ids in the community. Defaults to None.
            icon_url (str | None, optional): URL of image to use as community icon. Set to an empty string to remove.
                Defaults to None.
            local_only (bool | None, optional): Make the community local-only or not. Defaults to None.
            nsfw (bool | None, optional): Make the community entirely NSFW or not. Defaults to None.
            restricted_to_mods (bool | None, optional): Make the community only allow posts by mods. Defaults to None.
            question_answer (bool | None, optional): Make the community a question and answer community. Defaults to
                None.
            rules (str | None, optional): Rules field for the community. This field is deprecated. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id}

        if title is not None:
            data["title"] = title
        if description is not None:
            data["description"] = description
        if discussion_languages is not None:
            data["discussion_languages"] = discussion_languages
        if local_only is not None:
            data["local_only"] = local_only
        if nsfw is not None:
            data["nsfw"] = nsfw
        if restricted_to_mods is not None:
            data["restricted_to_mods"] = restricted_to_mods
        if question_answer is not None:
            data["question_answer"] = question_answer
        if rules is not None:
            data["rules"] = rules

        if banner_url is not None and banner_url != "":
            data["banner_url"] = banner_url
        elif banner_url == "":
            data["banner_url"] = None

        if icon_url is not None and icon_url != "":
            data["icon_url"] = icon_url
        elif icon_url == "":
            data["icon_url"] = None

        return self._client.request(method="PUT", endpoint="community", data=data)

    def list_communities(
        self,
        limit: int | None = None,
        page: int | None = None,
        show_nsfw: bool | None = None,
        sort: str | None = None,
        type_: str | None = None,
    ) -> dict | None:
        """Get a list of communities.

        API endpoint: GET community/list

        Args:
            limit (int | None, optional): Max number of communities to return on a page. Defaults to None.
            page (int | None, optional): The page of results to fetch. Defaults to None.
            show_nsfw (bool | None, optional): Include NSFW results or not. Defaults to None.
            sort (str | None, optional): Sorting method. See PieFed API documentation for details. Defaults to None.
            type_ (str | None, optional): Type filter. See PieFed API documentation for details. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if show_nsfw is not None:
            params["show_nsfw"] = show_nsfw
        if sort is not None:
            params["sort"] = sort
        if type_ is not None:
            params["type_"] = type_

        return self._client.request(method="GET", endpoint="community/list", params=params)

    def follow(self, community_id: int, follow: bool) -> dict | None:
        """Start following (join) to a community.

        API endpoint: POST community/follow

        Args:
            community_id (int): Communit id to join.
            follow (bool): True to join a community. False to leave it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "follow": follow}

        return self._client.request(method="POST", endpoint="community/follow", data=data)

    def leave_all(self) -> dict | None:
        """Leave all communities for which you are not a moderator.

        API endpoint: POST community/leave_all

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="POST", endpoint="community/leave_all")

    def block(self, community_id: int, block: bool) -> dict | None:
        """Block a community.

        API endpoint: POST community/block

        Args:
            community_id (int): Community id to block.
            block (bool): True to block the community. False to unblock it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "block": block}

        return self._client.request(method="POST", endpoint="community/block", data=data)

    def subscribe(self, community_id: int, subscribe: bool) -> dict | None:
        """Get notified of new posts in a community.

        API endpoint: PUT community/subscribe

        Args:
            community_id (int): Community id to receive notifications for new posts in.
            subscribe (bool): True to receive notifications. False to stop.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="community/subscribe", data=data)

    def delete(self, community_id: int, deleted: bool) -> dict | None:
        """Delete a community.

        API endpoint: POST community/delete

        Args:
            community_id (int): Community id of the community to delete.
            deleted (bool): True to delete the community. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="community/delete", data=data)

    def mod(self, community_id: int, person_id: int, added: bool) -> dict | None:
        """Add or remove a moderator.

        API endpoint: POST community/mod

        Args:
            community_id (int): Community id in which to appooint or remove a mod.
            person_id (int): User id of new or previous moderator.
            added (bool): True to appoint as a mod. False to remove them as a mod.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "person_id": person_id, "added": added}

        return self._client.request(method="POST", endpoint="community/mod", data=data)

    def list_bans(self, community_id: int, limit: int | None = None, page: int | None = None) -> dict | None:
        """List the banned users of a community.

        API endpoint: GET community/moderate/bans

        Args:
            community_id (int): Community id to list bans for.
            limit (int | None, optional): Max results on one page. Defaults to None.
            page (int | None, optional): Page number of results to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {"community_id": community_id}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return self._client.request(method="GET", endpoint="community/moderate/bans", params=params)

    def unban(self, community_id: int, user_id: int) -> dict | None:
        """Unban a user from a community.

        API endpoint: PUT community/moderate/unban

        Args:
            community_id (int): Community id from which the user is unbanned.
            user_id (int): User id of the user.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "user_id": user_id}

        return self._client.request(method="PUT", endpoint="community/moderate/unban", data=data)

    def ban_user(
        self,
        community_id: int,
        user_id: int,
        reason: str,
        expires_at: str | None = None,
        permanent: bool | None = None,
    ) -> dict | None:
        """Ban a user from a community.

        API endpoint: POST community/moderate/ban

        Args:
            community_id (int): Community id to ban the user from.
            user_id (int): User id of the user being banned.
            reason (str): Reason for the ban.
            expires_at (str | None, optional): Datetime string at which the ban ends. Defaults to None.
            permanent (bool | None, optional): If True, the ban is permanent. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "user_id": user_id, "reason": reason}

        if expires_at is not None:
            data["expires_at"] = expires_at
        if permanent is not None:
            data["permanent"] = permanent

        return self._client.request(method="POST", endpoint="community/moderate/ban", data=data)

    def moderate_post_nsfw(self, post_id: int, nsfw_status: bool) -> dict | None:
        """Mark or unmark a post as NSFW.

        API endpoint: POST community/moderate/post/nsfw

        Args:
            post_id (int): Post id being marked or unmarked.
            nsfw_status (bool): True to mark the post as NSFW. False to unmark it as NSFW.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "nsfw_status": nsfw_status}

        return self._client.request(method="POST", endpoint="community/moderate/post/nsfw", data=data)

    def create_flair(
        self,
        community_id: int,
        flair_title: str,
        text_color: str | None = None,
        background_color: str | None = None,
        blur_images: bool | None = None,
    ) -> dict | None:
        """Create a flair in a community.

        API endpoint: POST community/flair

        Args:
            community_id (int): Community id flair is being created in.
            flair_title (str): Displayed name of the flair
            text_color (str | None, optional): Hex code of the color of the text. Defaults to None.
            background_color (str | None, optional): Hex code of the color of the background. Defaults to None.
            blur_images (bool | None, optional): True if posts with this flair should have blurred images. False if this
                flair doesn't blur images. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "flair_title": flair_title}

        if text_color is not None:
            data["text_color"] = text_color
        if background_color is not None:
            data["background_color"] = background_color
        if blur_images is not None:
            data["blur_images"] = blur_images

        return self._client.request(method="POST", endpoint="community/flair", data=data)

    def edit_flair(
        self,
        flair_id: int,
        flair_title: str | None = None,
        text_color: str | None = None,
        background_color: str | None = None,
        blur_images: bool | None = None,
    ) -> dict | None:
        """Edit a flair in a community.

        API endpoint: PUT community/flair

        Args:
            flair_id (int): Flair id of the flair being edited.
            flair_title (str | None, optional): Displayed title of the flair. Defaults to None.
            text_color (str | None, optional): Hex code of the color of the text. Defaults to None.
            background_color (str | None, optional): Hex code of the color of the background. Defaults to None.
            blur_images (bool | None, optional): True if posts with this flair should have blurred images. False if this
                flair doesn't blur images. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"flair_id": flair_id}

        if flair_title is not None:
            data["flair_title"] = flair_title
        if text_color is not None:
            data["text_color"] = text_color
        if background_color is not None:
            data["background_color"] = background_color
        if blur_images is not None:
            data["blur_images"] = blur_images

        return self._client.request(method="PUT", endpoint="community/flair", data=data)

    def delete_flair(self, flair_id: int) -> dict | None:
        """Delete a flair in a community.

        API endpoint: POST community/flair/delete

        Args:
            flair_id (int): Flair id of the community flair to delete.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"flair_id": flair_id}

        return self._client.request(method="POST", endpoint="community/flair/delete", data=data)


class CommunityAsync:
    """Class to hold async Community endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def get(self, community_id: int | None = None, name: str | None = None) -> dict | None:
        """Get details for a single community.

        API endpoint: GET community

        Args:
            community_id (int | None, optional): Community id of the community to fetch. Defaults to None.
            name (str | None, optional): Name of the community to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if community_id is not None:
            params["id"] = community_id
        if name is not None:
            params["name"] = name

        return await self._client.request(method="GET", endpoint="community", params=params)

    async def create(
        self,
        name: str,
        title: str,
        banner_url: str | None = None,
        description: str | None = None,
        discussion_languages: list[int] | None = None,
        icon_url: str | None = None,
        local_only: bool | None = None,
        nsfw: bool | None = None,
        question_answer: bool | None = None,
        restricted_to_mods: bool | None = None,
        rules: str | None = None,
    ) -> dict | None:
        """Create a new community.

        API endpoint: POST community

        Args:
            name (str): Name of the community (part of url, so needs to be url-safe)
            title (str): Displayed title of the community.
            banner_url (str | None, optional): URL of image to use as community banner. Defaults to None.
            description (str | None, optional): Sidebar contents of the community in markdown. Defaults to None.
            discussion_languages (list[int] | None, optional): Allowed language ids for the community. Defaults to None.
            icon_url (str | None, optional): URL of image to use as community icon. Defaults to None.
            local_only (bool | None, optional): Make this community local-only. Defaults to None.
            nsfw (bool | None, optional): Make community entirely NSFW or not. Defaults to None.
            question_answer (bool | None, optional): Make community a question and answer community. Defaults to None.
            restricted_to_mods (bool | None, optional): Only allow posts by moderators. Defaults to None.
            rules (str | None, optional): Rules field for the community. This field is deprecated. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"name": name, "title": title}

        if banner_url is not None and banner_url != "":
            data["banner_url"] = banner_url
        elif banner_url == "":
            data["banner_url"] = None
        if description is not None:
            data["description"] = description
        if discussion_languages is not None:
            data["discussion_languages"] = discussion_languages
        if icon_url is not None and icon_url != "":
            data["icon_url"] = icon_url
        elif icon_url == "":
            data["icon_url"] = None
        if local_only is not None:
            data["local_only"] = local_only
        if nsfw is not None:
            data["nsfw"] = nsfw
        if question_answer is not None:
            data["question_answer"] = question_answer
        if restricted_to_mods is not None:
            data["restricted_to_mods"] = restricted_to_mods
        if rules is not None:
            data["rules"] = rules

        return await self._client.request(method="POST", endpoint="community", data=data)

    async def edit(
        self,
        community_id: int,
        title: str | None = None,
        banner_url: str | None = None,
        description: str | None = None,
        discussion_languages: list[int] | None = None,
        icon_url: str | None = None,
        local_only: bool | None = None,
        nsfw: bool | None = None,
        restricted_to_mods: bool | None = None,
        question_answer: bool | None = None,
        rules: str | None = None,
    ) -> dict | None:
        """Edit a community.

        API endpoint: PUT community

        Args:
            community_id (int): Community id of the community to edit.
            title (str | None, optional): Display title of the community. Set to an empty string to remove.
                Defaults to None.
            banner_url (str | None, optional): URL of image to use as community banner. Set to an empty string to
                remove. Defaults to None.
            description (str | None, optional): Sidebar contents of the community. Set to an empty string to remove.
                Defaults to None.
            discussion_languages (list[int] | None, optional): Allowed language ids in the community. Defaults to None.
            icon_url (str | None, optional): URL of image to use as community icon. Set to an empty string to remove.
                Defaults to None.
            local_only (bool | None, optional): Make the community local-only or not. Defaults to None.
            nsfw (bool | None, optional): Make the community entirely NSFW or not. Defaults to None.
            restricted_to_mods (bool | None, optional): Make the community only allow posts by mods. Defaults to None.
            question_answer (bool | None, optional): Make the community a question and answer community. Defaults to
                None.
            rules (str | None, optional): Rules field for the community. This field is deprecated. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id}

        if title is not None:
            data["title"] = title
        if banner_url is not None and banner_url != "":
            data["banner_url"] = banner_url
        elif banner_url == "":
            data["banner_url"] = None
        if description is not None:
            data["description"] = description
        if discussion_languages is not None:
            data["discussion_languages"] = discussion_languages
        if icon_url is not None and icon_url != "":
            data["icon_url"] = icon_url
        elif icon_url == "":
            data["icon_url"] = None
        if local_only is not None:
            data["local_only"] = local_only
        if nsfw is not None:
            data["nsfw"] = nsfw
        if restricted_to_mods is not None:
            data["restricted_to_mods"] = restricted_to_mods
        if question_answer is not None:
            data["question_answer"] = question_answer
        if rules is not None:
            data["rules"] = rules

        return await self._client.request(method="PUT", endpoint="community", data=data)

    async def list_communities(
        self,
        limit: int | None = None,
        page: int | None = None,
        show_nsfw: bool | None = None,
        sort: str | None = None,
        type_: str | None = None,
    ) -> dict | None:
        """Get a list of communities.

        API endpoint: GET community/list

        Args:
            limit (int | None, optional): Max number of communities to return on a page. Defaults to None.
            page (int | None, optional): The page of results to fetch. Defaults to None.
            show_nsfw (bool | None, optional): Include NSFW results or not. Defaults to None.
            sort (str | None, optional): Sorting method. See PieFed API documentation for details. Defaults to None.
            type_ (str | None, optional): Type filter. See PieFed API documentation for details. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if show_nsfw is not None:
            params["show_nsfw"] = show_nsfw
        if sort is not None:
            params["sort"] = sort
        if type_ is not None:
            params["type_"] = type_

        return await self._client.request(method="GET", endpoint="community/list", params=params)

    async def follow(self, community_id: int, follow: bool) -> dict | None:
        """Start following (join) to a community.

        API endpoint: POST community/follow

        Args:
            community_id (int): Communit id to join.
            follow (bool): True to join a community. False to leave it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "follow": follow}

        return await self._client.request(method="POST", endpoint="community/follow", data=data)

    async def leave_all(self) -> dict | None:
        """Leave all communities for which you are not a moderator.

        API endpoint: POST community/leave_all

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="POST", endpoint="community/leave_all")

    async def block(self, community_id: int, block: bool) -> dict | None:
        """Block a community.

        API endpoint: POST community/block

        Args:
            community_id (int): Community id to block.
            block (bool): True to block the community. False to unblock it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "block": block}

        return await self._client.request(method="POST", endpoint="community/block", data=data)

    async def subscribe(self, community_id: int, subscribe: bool) -> dict | None:
        """Get notified of new posts in a community.

        API endpoint: PUT community/subscribe

        Args:
            community_id (int): Community id to receive notifications for new posts in.
            subscribe (bool): True to receive notifications. False to stop.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="community/subscribe", data=data)

    async def delete(self, community_id: int, deleted: bool) -> dict | None:
        """Delete a community.

        API endpoint: POST community/delete

        Args:
            community_id (int): Community id of the community to delete.
            deleted (bool): True to delete the community. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="community/delete", data=data)

    async def mod(self, community_id: int, person_id: int, added: bool) -> dict | None:
        """Add or remove a moderator.

        API endpoint: POST community/mod

        Args:
            community_id (int): Community id in which to appooint or remove a mod.
            person_id (int): User id of new or previous moderator.
            added (bool): True to appoint as a mod. False to remove them as a mod.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "person_id": person_id, "added": added}

        return await self._client.request(method="POST", endpoint="community/mod", data=data)

    async def list_bans(self, community_id: int, limit: int | None = None, page: int | None = None) -> dict | None:
        """List the banned users of a community.

        API endpoint: GET community/moderate/bans

        Args:
            community_id (int): Community id to list bans for.
            limit (int | None, optional): Max results on one page. Defaults to None.
            page (int | None, optional): Page number of results to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {"community_id": community_id}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return await self._client.request(method="GET", endpoint="community/moderate/bans", params=params)

    async def unban(self, community_id: int, user_id: int) -> dict | None:
        """Unban a user from a community.

        API endpoint: PUT community/moderate/unban

        Args:
            community_id (int): Community id from which the user is unbanned.
            user_id (int): User id of the user.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "user_id": user_id}

        return await self._client.request(method="PUT", endpoint="community/moderate/unban", data=data)

    async def ban_user(
        self,
        community_id: int,
        user_id: int,
        reason: str,
        expires_at: str | None = None,
        permanent: bool | None = None,
    ) -> dict | None:
        """Ban a user from a community.

        API endpoint: POST community/moderate/ban

        Args:
            community_id (int): Community id to ban the user from.
            user_id (int): User id of the user being banned.
            reason (str): Reason for the ban.
            expires_at (str | None, optional): Datetime string at which the ban ends. Defaults to None.
            permanent (bool | None, optional): If True, the ban is permanent. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "user_id": user_id, "reason": reason}

        if expires_at is not None:
            data["expires_at"] = expires_at
        if permanent is not None:
            data["permanent"] = permanent

        return await self._client.request(method="POST", endpoint="community/moderate/ban", data=data)

    async def moderate_post_nsfw(self, post_id: int, nsfw_status: bool) -> dict | None:
        """Mark or unmark a post as NSFW.

        API endpoint: POST community/moderate/post/nsfw

        Args:
            post_id (int): Post id being marked or unmarked.
            nsfw_status (bool): True to mark the post as NSFW. False to unmark it as NSFW.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "nsfw_status": nsfw_status}

        return await self._client.request(method="POST", endpoint="community/moderate/post/nsfw", data=data)

    async def create_flair(
        self,
        community_id: int,
        flair_title: str,
        text_color: str | None = None,
        background_color: str | None = None,
        blur_images: bool | None = None,
    ) -> dict | None:
        """Create a flair in a community.

        API endpoint: POST community/flair

        Args:
            community_id (int): Community id flair is being created in.
            flair_title (str): Displayed name of the flair
            text_color (str | None, optional): Hex code of the color of the text. Defaults to None.
            background_color (str | None, optional): Hex code of the color of the background. Defaults to None.
            blur_images (bool | None, optional): True if posts with this flair should have blurred images. False if this
                flair doesn't blur images. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"community_id": community_id, "flair_title": flair_title}

        if text_color is not None:
            data["text_color"] = text_color
        if background_color is not None:
            data["background_color"] = background_color
        if blur_images is not None:
            data["blur_images"] = blur_images

        return await self._client.request(method="POST", endpoint="community/flair", data=data)

    async def edit_flair(
        self,
        flair_id: int,
        flair_title: str | None = None,
        text_color: str | None = None,
        background_color: str | None = None,
        blur_images: bool | None = None,
    ) -> dict | None:
        """Edit a flair in a community.

        API endpoint: PUT community/flair

        Args:
            flair_id (int): Flair id of the flair being edited.
            flair_title (str | None, optional): Displayed title of the flair. Defaults to None.
            text_color (str | None, optional): Hex code of the color of the text. Defaults to None.
            background_color (str | None, optional): Hex code of the color of the background. Defaults to None.
            blur_images (bool | None, optional): True if posts with this flair should have blurred images. False if this
                flair doesn't blur images. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"flair_id": flair_id}

        if flair_title is not None:
            data["flair_title"] = flair_title
        if text_color is not None:
            data["text_color"] = text_color
        if background_color is not None:
            data["background_color"] = background_color
        if blur_images is not None:
            data["blur_images"] = blur_images

        return await self._client.request(method="PUT", endpoint="community/flair", data=data)

    async def delete_flair(self, flair_id: int) -> dict | None:
        """Delete a flair in a community.

        API endpoint: POST community/flair/delete

        Args:
            flair_id (int): Flair id of the community flair to delete.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"flair_id": flair_id}

        return await self._client.request(method="POST", endpoint="community/flair/delete", data=data)
