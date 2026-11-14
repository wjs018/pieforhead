from .clients import PieFedClient, AsyncPieFedClient
from .exceptions import NotImplementedError


class Post:
    """Class to hold Post endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list_posts(
        self,
        query: str | None = None,
        sort: str | None = None,
        type_: str | None = None,
        community_name: str | None = None,
        community_id: int | None = None,
        saved_only: bool | None = None,
        nsfw: str | None = None,
        person_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        liked_only: bool | None = None,
        feed_id: int | None = None,
        topic_id: int | None = None,
        ignore_sticky: bool | None = None,
    ) -> dict | None:
        params = {}

        if query is not None:
            params["q"] = query
        if sort is not None:
            params["sort"] = sort
        if type_ is not None:
            params["type_"] = type_
        if community_name is not None:
            params["community_name"] = community_name
        if community_id is not None:
            params["community_id"] = community_id
        if saved_only is not None:
            params["saved_only"] = saved_only
        if nsfw is not None:
            params["nsfw"] = nsfw
        if person_id is not None:
            params["person_id"] = person_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if liked_only is not None:
            params["liked_only"] = liked_only
        if feed_id is not None:
            params["feed_id"] = feed_id
        if topic_id is not None:
            params["topic_id"] = topic_id
        if ignore_sticky is not None:
            params["ignore_sticky"] = ignore_sticky

        return self._client.request(method="GET", endpoint="post/list", params=params)

    def list_posts_2(self):
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    def list_scheduled(
        self,
        query: str | None = None,
        sort: str | None = None,
        community_name: str | None = None,
        community_id: int | None = None,
        include_deleted: bool | None = None,
        limit: int | None = None,
        page: int | None = None,
    ) -> dict | None:
        params = {}

        if query is not None:
            params["q"] = query
        if sort is not None:
            params["sort"] = sort
        if community_name is not None:
            params["community_name"] = community_name
        if community_id is not None:
            params["community_id"] = community_id
        if include_deleted is not None:
            params["include_deleted"] = include_deleted
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return self._client.request(method="GET", endpoint="post/scheduled/list", params=params)

    def get(self, post_id: int) -> dict | None:
        return self._client.request(method="GET", endpoint="post", params={"id": post_id})

    def create(
        self,
        title: str,
        community_id: int,
        alt_text: str | None = None,
        body: str | None = None,
        url: str | None = None,
        og_image_url: str | None = None,
        nsfw: bool | None = None,
        ai_generated: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
    ) -> dict | None:
        data = {"title": title, "community_id": community_id}

        if alt_text is not None:
            data["alt_text"] = alt_text
        if body is not None:
            data["body"] = body
        if url is not None:
            data["url"] = url
        if og_image_url is not None:
            data["og_image_url"] = og_image_url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if ai_generated is not None:
            data["ai_generated"] = ai_generated
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll

        return self._client.request(method="POST", endpoint="post", data=data)

    def edit(
        self,
        post_id: int,
        alt_text: str | None = None,
        title: str | None = None,
        body: str | None = None,
        url: str | None = None,
        nsfw: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        tags: str | None = None,
        flair: str | None = None,
    ) -> dict | None:
        data = {"post_id": post_id}

        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
        if nsfw is not None:
            data["nsfw"] = nsfw
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll

        if alt_text is not None and alt_text != "":
            data["alt_text"] = alt_text
        elif alt_text == "":
            data["alt_text"] = None

        if url is not None and url != "":
            data["url"] = url
        elif url == "":
            data["url"] = None

        if tags is not None and tags != "":
            data["tags"] = tags
        elif tags == "":
            data["tags"] = None

        if flair is not None and flair != "":
            data["flair"] = flair
        elif flair == "":
            data["flair"] = None

        return self._client.request(method="PUT", endpoint="post", data=data)

    def get_scheduled(self, post_id: int) -> dict | None:
        return self._client.request(method="GET", endpoint="post/scheduled", params={"id": post_id})

    def create_scheduled(
        self,
        title: str,
        community_id: int,
        scheduled_for: str,
        alt_text: str | None = None,
        body: str | None = None,
        url: str | None = None,
        og_image_url: str | None = None,
        nsfw: bool | None = None,
        ai_generated: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        repeat: str | None = None,
    ) -> dict | None:
        data = {"title": title, "community_id": community_id, "scheduled_for": scheduled_for}

        if alt_text is not None:
            data["alt_text"] = alt_text
        if body is not None:
            data["body"] = body
        if url is not None:
            data["url"] = url
        if og_image_url is not None:
            data["og_image_url"] = og_image_url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if ai_generated is not None:
            data["ai_generated"] = ai_generated
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll
        if repeat is not None:
            data["repeat"] = repeat

        return self._client.request(method="POST", endpoint="post/scheduled", data=data)

    def edit_scheduled(
        self,
        post_id: int,
        alt_text: str | None = None,
        title: str | None = None,
        body: str | None = None,
        url: str | None = None,
        nsfw: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        tags: str | None = None,
        flair: str | None = None,
        scheduled_for: str | None = None,
        repeat: str | None = None,
    ) -> dict | None:
        data = {"post_id": post_id}

        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
        if nsfw is not None:
            data["nsfw"] = nsfw
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll
        if scheduled_for is not None:
            data["scheduled_for"] = scheduled_for
        if repeat is not None:
            data["repeat"] = repeat

        if alt_text is not None and alt_text != "":
            data["alt_text"] = alt_text
        elif alt_text == "":
            data["alt_text"] = None

        if url is not None and url != "":
            data["url"] = url
        elif url == "":
            data["url"] = None

        if tags is not None and tags != "":
            data["tags"] = tags
        elif tags == "":
            data["tags"] = None

        if flair is not None and flair != "":
            data["flair"] = flair
        elif flair == "":
            data["flair"] = None

        return self._client.request(method="PUT", endpoint="post/scheduled", data=data)

    def replies(
        self,
        post_id: int | None = None,
        parent_id: int | None = None,
        sort: str | None = None,
        max_depth: int | None = None,
        page: str | None = None,
        limit: int | None = None,
    ) -> dict | None:
        params = {}

        if post_id is not None:
            params["post_id"] = post_id
        if parent_id is not None:
            params["parent_id"] = parent_id
        if sort is not None:
            params["sort"] = sort
        if max_depth is not None:
            params["max_depth"] = max_depth
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return self._client.request(method="GET", endpoint="post/replies", params=params)

    def site_metadata(self, url: str) -> dict | None:
        return self._client.request(method="GET", endpoint="post/site_metadata", params={"url": url})

    def like(self, post_id: int, score: int, private: bool | None = None, emoji: str | None = None) -> dict | None:
        data = {"post_id": post_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return self._client.request(method="POST", endpoint="post/like", data=data)

    def save(self, post_id: int, save: bool) -> dict | None:
        return self._client.request(method="PUT", endpoint="post/save", data={"post_id": post_id, "save": save})

    def subscribe(self, post_id: int, subscribe: bool) -> dict | None:
        data = {"post_id": post_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="post/subscribe", data=data)

    def delete(self, post_id: int, deleted: bool) -> dict | None:
        data = {"post_id": post_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="post/delete", data=data)

    def delete_scheduled(self, post_id: int, deleted: bool) -> dict | None:
        data = {"post_id": post_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="post/scheduled/delete", data=data)

    def report(
        self,
        post_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        data = {"post_id": post_id, "reason": reason}

        if description is not None:
            data["description"] = description
        if report_remote is not None:
            data["report_remote"] = report_remote

        return self._client.request(method="POST", endpoint="post/report", data=data)

    def list_reports(
        self,
        community_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        post_id: int | None = None,
        unresolved_only: bool | None = None,
    ) -> dict | None:
        params = {}

        if community_id is not None:
            params["community_id"] = community_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if post_id is not None:
            params["post_id"] = post_id
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only

        return self._client.request(method="GET", endpoint="post/report/list", params=params)

    def resolve_report(self, report_id: int, resolved: bool) -> dict | None:
        data = {"report_id": report_id, "resolved": resolved}

        return self._client.request(method="PUT", endpoint="post/report/resolve", data=data)

    def lock(self, post_id: int, locked: bool) -> dict | None:
        return self._client.request(method="POST", endpoint="post/lock", data={"post_id": post_id, "locked": locked})

    def hide(self, post_id: int, hidden: bool) -> dict | None:
        return self._client.request(method="POST", endpoint="post/hide", data={"post_id": post_id, "hidden": hidden})

    def feature(self, post_id: int, featured: bool, feature_type: str | None = None) -> dict | None:
        data = {"post_id": post_id, "featured": featured}

        if feature_type is not None:
            data["feature_type"] = feature_type

        return self._client.request(method="POST", endpoint="post/feature", data=data)

    def remove(self, post_id: int, removed: bool, reason: str | None = None) -> dict | None:
        data = {"post_id": post_id, "removed": removed}

        if reason is not None:
            data["reason"] = reason

        return self._client.request(method="POST", endpoint="post/remove", data=data)

    def mark_as_read(
        self,
        read: bool,
        post_id: int | None = None,
        post_ids: list[int] | None = None,
    ) -> dict | None:
        data = {"read": read}

        if post_id is not None:
            data["post_id"] = post_id
        if post_ids is not None:
            data["post_ids"] = post_ids

        return self._client.request(method="POST", endpoint="post/mark_as_read", data=data)

    def list_likes(self, post_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        params = {"post_id": post_id}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return self._client.request(method="GET", endpoint="post/like/list", params=params)

    def assign_flair(self, post_id: int, flair_id_list: list[int] | None = None) -> dict | None:
        data = {"post_id": post_id}

        if flair_id_list is not None and flair_id_list != []:
            data["flair_id_list"] = flair_id_list
        elif flair_id_list == []:
            data["flair_id_list"] = None

        return self._client.request(method="POST", endpoint="post/assign_flair", data=data)

    def poll_vote(self, post_id: int, choice_id: list[int]) -> dict | None:
        data = {"post_id": post_id, "choice_id": choice_id}

        return self._client.request(method="POST", endpoint="post/poll_vote", data=data)


class PostAsync:
    """Class to hold async Post endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def list_posts(
        self,
        query: str | None = None,
        sort: str | None = None,
        type_: str | None = None,
        community_name: str | None = None,
        community_id: int | None = None,
        saved_only: bool | None = None,
        nsfw: str | None = None,
        person_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        liked_only: bool | None = None,
        feed_id: int | None = None,
        topic_id: int | None = None,
        ignore_sticky: bool | None = None,
    ) -> dict | None:
        params = {}

        if query is not None:
            params["q"] = query
        if sort is not None:
            params["sort"] = sort
        if type_ is not None:
            params["type_"] = type_
        if community_name is not None:
            params["community_name"] = community_name
        if community_id is not None:
            params["community_id"] = community_id
        if saved_only is not None:
            params["saved_only"] = saved_only
        if nsfw is not None:
            params["nsfw"] = nsfw
        if person_id is not None:
            params["person_id"] = person_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if liked_only is not None:
            params["liked_only"] = liked_only
        if feed_id is not None:
            params["feed_id"] = feed_id
        if topic_id is not None:
            params["topic_id"] = topic_id
        if ignore_sticky is not None:
            params["ignore_sticky"] = ignore_sticky

        return await self._client.request(method="GET", endpoint="post/list", params=params)

    async def list_posts_2(self):
        if self._client.raise_exceptions:
            raise NotImplementedError
        else:
            return

    async def list_scheduled(
        self,
        query: str | None = None,
        sort: str | None = None,
        community_name: str | None = None,
        community_id: int | None = None,
        include_deleted: bool | None = None,
        limit: int | None = None,
        page: int | None = None,
    ) -> dict | None:
        params = {}

        if query is not None:
            params["q"] = query
        if sort is not None:
            params["sort"] = sort
        if community_name is not None:
            params["community_name"] = community_name
        if community_id is not None:
            params["community_id"] = community_id
        if include_deleted is not None:
            params["include_deleted"] = include_deleted
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page

        return await self._client.request(method="GET", endpoint="post/scheduled/list", params=params)

    async def get(self, post_id: int) -> dict | None:
        return await self._client.request(method="GET", endpoint="post", params={"id": post_id})

    async def create(
        self,
        title: str,
        community_id: int,
        alt_text: str | None = None,
        body: str | None = None,
        url: str | None = None,
        og_image_url: str | None = None,
        nsfw: bool | None = None,
        ai_generated: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
    ) -> dict | None:
        data = {"title": title, "community_id": community_id}

        if alt_text is not None:
            data["alt_text"] = alt_text
        if body is not None:
            data["body"] = body
        if url is not None:
            data["url"] = url
        if og_image_url is not None:
            data["og_image_url"] = og_image_url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if ai_generated is not None:
            data["ai_generated"] = ai_generated
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll

        return await self._client.request(method="POST", endpoint="post", data=data)

    async def edit(
        self,
        post_id: int,
        alt_text: str | None = None,
        title: str | None = None,
        body: str | None = None,
        url: str | None = None,
        nsfw: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        tags: str | None = None,
        flair: str | None = None,
    ) -> dict | None:
        data = {"post_id": post_id}

        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
        if nsfw is not None:
            data["nsfw"] = nsfw
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll

        if alt_text is not None and alt_text != "":
            data["alt_text"] = alt_text
        elif alt_text == "":
            data["alt_text"] = None

        if url is not None and url != "":
            data["url"] = url
        elif url == "":
            data["url"] = None

        if tags is not None and tags != "":
            data["tags"] = tags
        elif tags == "":
            data["tags"] = None

        if flair is not None and flair != "":
            data["flair"] = flair
        elif flair == "":
            data["flair"] = None

        return await self._client.request(method="PUT", endpoint="post", data=data)

    async def get_scheduled(self, post_id: int) -> dict | None:
        return await self._client.request(method="GET", endpoint="post/scheduled", params={"id": post_id})

    async def create_scheduled(
        self,
        title: str,
        community_id: int,
        scheduled_for: str,
        alt_text: str | None = None,
        body: str | None = None,
        url: str | None = None,
        og_image_url: str | None = None,
        nsfw: bool | None = None,
        ai_generated: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        repeat: str | None = None,
    ) -> dict | None:
        data = {"title": title, "community_id": community_id, "scheduled_for": scheduled_for}

        if alt_text is not None:
            data["alt_text"] = alt_text
        if body is not None:
            data["body"] = body
        if url is not None:
            data["url"] = url
        if og_image_url is not None:
            data["og_image_url"] = og_image_url
        if nsfw is not None:
            data["nsfw"] = nsfw
        if ai_generated is not None:
            data["ai_generated"] = ai_generated
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll
        if repeat is not None:
            data["repeat"] = repeat

        return await self._client.request(method="POST", endpoint="post/scheduled", data=data)

    async def edit_scheduled(
        self,
        post_id: int,
        alt_text: str | None = None,
        title: str | None = None,
        body: str | None = None,
        url: str | None = None,
        nsfw: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        tags: str | None = None,
        flair: str | None = None,
        scheduled_for: str | None = None,
        repeat: str | None = None,
    ) -> dict | None:
        data = {"post_id": post_id}

        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
        if nsfw is not None:
            data["nsfw"] = nsfw
        if language_id is not None:
            data["language_id"] = language_id
        if event is not None:
            data["event"] = event
        if poll is not None:
            data["poll"] = poll
        if scheduled_for is not None:
            data["scheduled_for"] = scheduled_for
        if repeat is not None:
            data["repeat"] = repeat

        if alt_text is not None and alt_text != "":
            data["alt_text"] = alt_text
        elif alt_text == "":
            data["alt_text"] = None

        if url is not None and url != "":
            data["url"] = url
        elif url == "":
            data["url"] = None

        if tags is not None and tags != "":
            data["tags"] = tags
        elif tags == "":
            data["tags"] = None

        if flair is not None and flair != "":
            data["flair"] = flair
        elif flair == "":
            data["flair"] = None

        return await self._client.request(method="PUT", endpoint="post/scheduled", data=data)

    async def replies(
        self,
        post_id: int | None = None,
        parent_id: int | None = None,
        sort: str | None = None,
        max_depth: int | None = None,
        page: str | None = None,
        limit: int | None = None,
    ) -> dict | None:
        params = {}

        if post_id is not None:
            params["post_id"] = post_id
        if parent_id is not None:
            params["parent_id"] = parent_id
        if sort is not None:
            params["sort"] = sort
        if max_depth is not None:
            params["max_depth"] = max_depth
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="post/replies", params=params)

    async def site_metadata(self, url: str) -> dict | None:
        return await self._client.request(method="GET", endpoint="post/site_metadata", params={"url": url})

    async def like(
        self,
        post_id: int,
        score: int,
        private: bool | None = None,
        emoji: str | None = None,
    ) -> dict | None:
        data = {"post_id": post_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return await self._client.request(method="POST", endpoint="post/like", data=data)

    async def save(self, post_id: int, save: bool) -> dict | None:
        return await self._client.request(method="PUT", endpoint="post/save", data={"post_id": post_id, "save": save})

    async def subscribe(self, post_id: int, subscribe: bool) -> dict | None:
        data = {"post_id": post_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="post/subscribe", data=data)

    async def delete(self, post_id: int, deleted: bool) -> dict | None:
        data = {"post_id": post_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="post/delete", data=data)

    async def delete_scheduled(self, post_id: int, deleted: bool) -> dict | None:
        data = {"post_id": post_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="post/scheduled/delete", data=data)

    async def report(
        self,
        post_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        data = {"post_id": post_id, "reason": reason}

        if description is not None:
            data["description"] = description
        if report_remote is not None:
            data["report_remote"] = report_remote

        return await self._client.request(method="POST", endpoint="post/report", data=data)

    async def list_reports(
        self,
        community_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        post_id: int | None = None,
        unresolved_only: bool | None = None,
    ) -> dict | None:
        params = {}

        if community_id is not None:
            params["community_id"] = community_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if post_id is not None:
            params["post_id"] = post_id
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only

        return await self._client.request(method="GET", endpoint="post/report/list", params=params)

    async def resolve_report(self, report_id: int, resolved: bool) -> dict | None:
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(method="PUT", endpoint="post/report/resolve", data=data)

    async def lock(self, post_id: int, locked: bool) -> dict | None:
        return await self._client.request(
            method="POST",
            endpoint="post/lock",
            data={"post_id": post_id, "locked": locked},
        )

    async def hide(self, post_id: int, hidden: bool) -> dict | None:
        data = {"post_id": post_id, "hidden": hidden}

        return await self._client.request(method="POST", endpoint="post/hide", data=data)

    async def feature(self, post_id: int, featured: bool, feature_type: str | None = None) -> dict | None:
        data = {"post_id": post_id, "featured": featured}

        if feature_type is not None:
            data["feature_type"] = feature_type

        return await self._client.request(method="POST", endpoint="post/feature", data=data)

    async def remove(self, post_id: int, removed: bool, reason: str | None = None) -> dict | None:
        data = {"post_id": post_id, "removed": removed}

        if reason is not None:
            data["reason"] = reason

        return await self._client.request(method="POST", endpoint="post/remove", data=data)

    async def mark_as_read(
        self,
        read: bool,
        post_id: int | None = None,
        post_ids: list[int] | None = None,
    ) -> dict | None:
        data = {"read": read}

        if post_id is not None:
            data["post_id"] = post_id
        if post_ids is not None:
            data["post_ids"] = post_ids

        return await self._client.request(method="POST", endpoint="post/mark_as_read", data=data)

    async def list_likes(self, post_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        params = {"post_id": post_id}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="post/like/list", params=params)

    async def assign_flair(self, post_id: int, flair_id_list: list[int] | None = None) -> dict | None:
        data = {"post_id": post_id}

        if flair_id_list is not None and flair_id_list != []:
            data["flair_id_list"] = flair_id_list
        elif flair_id_list == []:
            data["flair_id_list"] = None

        return await self._client.request(method="POST", endpoint="post/assign_flair", data=data)

    async def poll_vote(self, post_id: int, choice_id: list[int]) -> dict | None:
        data = {"post_id": post_id, "choice_id": choice_id}

        return await self._client.request(method="POST", endpoint="post/poll_vote", data=data)
