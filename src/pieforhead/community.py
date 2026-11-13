from .clients import PieFedClient, AsyncPieFedClient


class Community:
    """Class to hold Community endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def get(self, community_id: int | None = None, name: str | None = None) -> dict | None:
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

    def list(
        self,
        limit: int | None = None,
        page: int | None = None,
        show_nsfw: bool | None = None,
        sort: str | None = None,
        type_: str | None = None,
    ) -> dict | None:
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
        data = {"community_id": community_id, "follow": follow}

        return self._client.request(method="POST", endpoint="community/follow", data=data)

    def leave_all(self) -> dict | None:
        return self._client.request(method="POST", endpoint="community/leave_all")

    def block(self, community_id: int, block: bool) -> dict | None:
        data = {"community_id": community_id, "block": block}

        return self._client.request(method="POST", endpoint="community/block", data=data)

    def subscribe(self, community_id: int, subscribe: bool) -> dict | None:
        data = {"community_id": community_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="community/subscribe", data=data)

    def delete(self, community_id: int, deleted: bool) -> dict | None:
        data = {"community_id": community_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="community/delete", data=data)

    def mod(self, community_id: int, person_id: int, added: bool) -> dict | None:
        data = {"community_id": community_id, "person_id": person_id, "added": added}

        return self._client.request(method="POST", endpoint="community/mod", data=data)

    def list_bans(self, community_id: int, limit: int | None = None, page: int | None = None) -> dict | None:
        params = {"community_id": community_id}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return self._client.request(method="GET", endpoint="community/moderate/bans", params=params)

    def unban(self, community_id: int, user_id: int) -> dict | None:
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
        data = {"community_id": community_id, "user_id": user_id, "reason": reason}

        if expires_at is not None:
            data["expires_at"] = expires_at
        if permanent is not None:
            data["permanent"] = permanent

        return self._client.request(method="POST", endpoint="community/moderate/ban", data=data)

    def moderate_post_nsfw(self, post_id: int, nsfw_status: bool) -> dict | None:
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
        data = {"flair_id": flair_id}

        return self._client.request(method="POST", endpoint="community/flair/delete", data=data)


class CommunityAsync:
    """Class to hold async Community endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def get(self, community_id: int | None = None, name: str | None = None) -> dict | None:
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

    async def list(
        self,
        limit: int | None = None,
        page: int | None = None,
        show_nsfw: bool | None = None,
        sort: str | None = None,
        type_: str | None = None,
    ) -> dict | None:
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
        data = {"community_id": community_id, "follow": follow}

        return await self._client.request(method="POST", endpoint="community/follow", data=data)

    async def leave_all(self) -> dict | None:
        return await self._client.request(method="POST", endpoint="community/leave_all")

    async def block(self, community_id: int, block: bool) -> dict | None:
        data = {"community_id": community_id, "block": block}

        return await self._client.request(method="POST", endpoint="community/block", data=data)

    async def subscribe(self, community_id: int, subscribe: bool) -> dict | None:
        data = {"community_id": community_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="community/subscribe", data=data)

    async def delete(self, community_id: int, deleted: bool) -> dict | None:
        data = {"community_id": community_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="community/delete", data=data)

    async def mod(self, community_id: int, person_id: int, added: bool) -> dict | None:
        data = {"community_id": community_id, "person_id": person_id, "added": added}

        return await self._client.request(method="POST", endpoint="community/mod", data=data)

    async def list_bans(self, community_id: int, limit: int | None = None, page: int | None = None) -> dict | None:
        params = {"community_id": community_id}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return await self._client.request(method="GET", endpoint="community/moderate/bans", params=params)

    async def unban(self, community_id: int, user_id: int) -> dict | None:
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
        data = {"community_id": community_id, "user_id": user_id, "reason": reason}

        if expires_at is not None:
            data["expires_at"] = expires_at
        if permanent is not None:
            data["permanent"] = permanent

        return await self._client.request(method="POST", endpoint="community/moderate/ban", data=data)

    async def moderate_post_nsfw(self, post_id: int, nsfw_status: bool) -> dict | None:
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
        data = {"flair_id": flair_id}

        return await self._client.request(method="POST", endpoint="community/flair/delete", data=data)
