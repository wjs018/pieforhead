from .clients import PieFedClient, AsyncPieFedClient


class Comment:
    """Class to hold Comment endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list_comments(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        type_: str | None = None,
        liked_only: bool | None = None,
        saved_only: bool | None = None,
        person_id: int | None = None,
        community_id: int | None = None,
        post_id: int | None = None,
        parent_id: int | None = None,
        max_depth: int | None = None,
        depth_first: bool | None = None,
    ) -> dict | None:
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if type_ is not None:
            params["type_"] = type_
        if liked_only is not None:
            params["liked_only"] = liked_only
        if saved_only is not None:
            params["saved_only"] = saved_only
        if person_id is not None:
            params["person_id"] = person_id
        if community_id is not None:
            params["community_id"] = community_id
        if post_id is not None:
            params["post_id"] = post_id
        if parent_id is not None:
            params["parent_id"] = parent_id
        if max_depth is not None:
            params["max_depth"] = max_depth
        if depth_first is not None:
            params["depth_first"] = depth_first

        return self._client.request(method="GET", endpoint="comment/list", params=params)

    def get(self, comment_id: int) -> dict | None:
        return self._client.request(method="GET", endpoint="comment", params={"id": comment_id})

    def create(
        self,
        body: str,
        post_id: int,
        parent_id: int | None = None,
        language_id: int | None = None,
    ) -> dict | None:
        data = {"body": body, "post_id": post_id}

        if parent_id is not None:
            data["parent_id"] = parent_id
        if language_id is not None:
            data["language_id"] = language_id

        return self._client.request(method="POST", endpoint="comment", data=data)

    def edit(
        self,
        comment_id: int,
        body: str,
        language_id: int | None = None,
        distinguished: bool | None = None,
    ) -> dict | None:
        data = {"comment_id": comment_id, "body": body}

        if language_id is not None:
            data["language_id"] = language_id
        if distinguished is not None:
            data["distinguished"] = distinguished

        return self._client.request(method="PUT", endpoint="comment", data=data)

    def like(self, comment_id: int, score: int, private: bool | None = None, emoji: str | None = None) -> dict | None:
        data = {"comment_id": comment_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return self._client.request(method="POST", endpoint="comment/like", data=data)

    def save(self, comment_id: int, save: bool) -> dict | None:
        data = {"comment_id": comment_id, "save": save}

        return self._client.request(method="PUT", endpoint="comment/save", data=data)

    def subscribe(self, comment_id: int, subscribe: bool) -> dict | None:
        data = {"comment_id": comment_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="comment/subscribe", data=data)

    def delete(self, comment_id: int, deleted: bool) -> dict | None:
        data = {"comment_id": comment_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="comment/delete", data=data)

    def report(
        self,
        comment_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        data = {"comment_id": comment_id, "reason": reason}

        if description is not None:
            data["description"] = description
        if report_remote is not None:
            data["report_remote"] = report_remote

        return self._client.request(method="POST", endpoint="comment/report", data=data)

    def list_reports(
        self,
        comment_id: int | None = None,
        community_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        unresolved_only: bool | None = None,
    ) -> dict | None:
        params = {}

        if comment_id is not None:
            params["comment_id"] = comment_id
        if community_id is not None:
            params["community_id"] = community_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only

        return self._client.request(method="GET", endpoint="comment/report/list", params=params)

    def resolve_report(self, report_id: int, resolved: bool) -> dict | None:
        data = {"report_id": report_id, "resolved": resolved}

        return self._client.request(method="PUT", endpoint="comment/report/resolve", data=data)

    def remove(self, comment_id: int, removed: bool, reason: str | None = None) -> dict | None:
        data = {"comment_id": comment_id, "removed": removed}

        if reason is not None:
            data["reason"] = reason

        return self._client.request(method="POST", endpoint="comment/remove", data=data)

    def mark_as_read(self, comment_reply_id: int, read: bool) -> dict | None:
        data = {"comment_reply_id": comment_reply_id, "read": read}

        return self._client.request(method="POST", endpoint="comment/mark_as_read", data=data)

    def mark_as_answer(self, comment_reply_id: int, answer: bool) -> dict | None:
        data = {"comment_reply_id": comment_reply_id, "answer": answer}

        return self._client.request(method="POST", endpoint="comment/mark_as_answer", data=data)

    def distinguish(self, comment_reply_id: int, distinguished: bool) -> dict | None:
        data = {"comment_reply_id": comment_reply_id, "distinguished": distinguished}

        return self._client.request(method="POST", endpoint="comment/distinguish", data=data)

    def lock(self, comment_id: int, locked: bool) -> dict | None:
        data = {"comment_id": comment_id, "locked": locked}

        return self._client.request(method="POST", endpoint="comment/lock", data=data)

    def list_likes(self, comment_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        params = {"comment_id": comment_id}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return self._client.request(method="GET", endpoint="comment/like/list", params=params)


class CommentAsync:
    """Class to hold async Comment endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def list_comments(
        self,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        type_: str | None = None,
        liked_only: bool | None = None,
        saved_only: bool | None = None,
        person_id: int | None = None,
        community_id: int | None = None,
        post_id: int | None = None,
        parent_id: int | None = None,
        max_depth: int | None = None,
        depth_first: bool | None = None,
    ) -> dict | None:
        params = {}

        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if type_ is not None:
            params["type_"] = type_
        if liked_only is not None:
            params["liked_only"] = liked_only
        if saved_only is not None:
            params["saved_only"] = saved_only
        if person_id is not None:
            params["person_id"] = person_id
        if community_id is not None:
            params["community_id"] = community_id
        if post_id is not None:
            params["post_id"] = post_id
        if parent_id is not None:
            params["parent_id"] = parent_id
        if max_depth is not None:
            params["max_depth"] = max_depth
        if depth_first is not None:
            params["depth_first"] = depth_first

        return await self._client.request(method="GET", endpoint="comment/list", params=params)

    async def get(self, comment_id: int) -> dict | None:
        return await self._client.request(method="GET", endpoint="comment", params={"id": comment_id})

    async def create(
        self,
        body: str,
        post_id: int,
        parent_id: int | None = None,
        language_id: int | None = None,
    ) -> dict | None:
        data = {"body": body, "post_id": post_id}

        if parent_id is not None:
            data["parent_id"] = parent_id
        if language_id is not None:
            data["language_id"] = language_id

        return await self._client.request(method="POST", endpoint="comment", data=data)

    async def edit(
        self,
        comment_id: int,
        body: str,
        language_id: int | None = None,
        distinguished: bool | None = None,
    ) -> dict | None:
        data = {"comment_id": comment_id, "body": body}

        if language_id is not None:
            data["language_id"] = language_id
        if distinguished is not None:
            data["distinguished"] = distinguished

        return await self._client.request(method="PUT", endpoint="comment", data=data)

    async def like(
        self, comment_id: int, score: int, private: bool | None = None, emoji: str | None = None
    ) -> dict | None:
        data = {"comment_id": comment_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return await self._client.request(method="POST", endpoint="comment/like", data=data)

    async def save(self, comment_id: int, save: bool) -> dict | None:
        data = {"comment_id": comment_id, "save": save}

        return await self._client.request(method="PUT", endpoint="comment/save", data=data)

    async def subscribe(self, comment_id: int, subscribe: bool) -> dict | None:
        data = {"comment_id": comment_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="comment/subscribe", data=data)

    async def delete(self, comment_id: int, deleted: bool) -> dict | None:
        data = {"comment_id": comment_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="comment/delete", data=data)

    async def report(
        self,
        comment_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        data = {"comment_id": comment_id, "reason": reason}

        if description is not None:
            data["description"] = description
        if report_remote is not None:
            data["report_remote"] = report_remote

        return await self._client.request(method="POST", endpoint="comment/report", data=data)

    async def list_reports(
        self,
        comment_id: int | None = None,
        community_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        unresolved_only: bool | None = None,
    ) -> dict | None:
        params = {}

        if comment_id is not None:
            params["comment_id"] = comment_id
        if community_id is not None:
            params["community_id"] = community_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only

        return await self._client.request(method="GET", endpoint="comment/report/list", params=params)

    async def resolve_report(self, report_id: int, resolved: bool) -> dict | None:
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(method="PUT", endpoint="comment/report/resolve", data=data)

    async def remove(self, comment_id: int, removed: bool, reason: str | None = None) -> dict | None:
        data = {"comment_id": comment_id, "removed": removed}

        if reason is not None:
            data["reason"] = reason

        return await self._client.request(method="POST", endpoint="comment/remove", data=data)

    async def mark_as_read(self, comment_reply_id: int, read: bool) -> dict | None:
        data = {"comment_reply_id": comment_reply_id, "read": read}

        return await self._client.request(method="POST", endpoint="comment/mark_as_read", data=data)

    async def mark_as_answer(self, comment_reply_id: int, answer: bool) -> dict | None:
        data = {"comment_reply_id": comment_reply_id, "answer": answer}

        return await self._client.request(method="POST", endpoint="comment/mark_as_answer", data=data)

    async def distinguish(self, comment_reply_id: int, distinguished: bool) -> dict | None:
        data = {"comment_reply_id": comment_reply_id, "distinguished": distinguished}

        return await self._client.request(method="POST", endpoint="comment/distinguish", data=data)

    async def lock(self, comment_id: int, locked: bool) -> dict | None:
        data = {"comment_id": comment_id, "locked": locked}

        return await self._client.request(method="POST", endpoint="comment/lock", data=data)

    async def list_likes(self, comment_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        params = {"comment_id": comment_id}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="comment/like/list", params=params)
