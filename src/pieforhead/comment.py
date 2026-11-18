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
        """Get list of comments.

        API endpoint: GET comment/list

        Args:
            limit (int | None, optional): Max number to return for a page of results. Defaults to None.
            page (int | None, optional): Page of results to request. Defaults to None.
            sort (str | None, optional): Sorting method for the returned comments. Defaults to None.
            type_ (str | None, optional): Type filter (Subscribed, Local, etc.). Defaults to None.
            liked_only (bool | None, optional): Only return liked comments. Defaults to None.
            saved_only (bool | None, optional): Only return saved comments. Defaults to None.
            person_id (int | None, optional): Filter to comments by a specific user. Defaults to None.
            community_id (int | None, optional): Filter to comments in a specific community. Defaults to None.
            post_id (int | None, optional): Filter to comments on a specific post. Defaults to None.
            parent_id (int | None, optional): Filter to replies to a specific comment. Defaults to None.
            max_depth (int | None, optional): Max number of nested levels to return. Defaults to None.
            depth_first (bool | None, optional): Guarantee parent comments are on the same page as any fetched comments.
                Defaults to None.

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
        """Get info for a single comment.

        API endpoint: GET comment

        Args:
            comment_id (int): Comment id of the comment to retrieve.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="comment", params={"id": comment_id})

    def create(
        self,
        body: str,
        post_id: int,
        parent_id: int | None = None,
        language_id: int | None = None,
    ) -> dict | None:
        """Create a comment.

        API endpoint: POST comment

        Args:
            body (str): Content of the comment in markdown.
            post_id (int): Post id that the comment is replying to.
            parent_id (int | None, optional): Parent comment id if the comment is a reply to another comment. Defaults
                to None.
            language_id (int | None, optional): Language id of the comment. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Edit a comment

        API endpoint: PUT comment

        Args:
            comment_id (int): The comment id of the comment to edit.
            body (str): New, edited content of the body in markdown.
            language_id (int | None, optional): Language id of the comment. Defaults to None.
            distinguished (bool | None, optional): Distinguish the comment as written by a moderator. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "body": body}

        if language_id is not None:
            data["language_id"] = language_id
        if distinguished is not None:
            data["distinguished"] = distinguished

        return self._client.request(method="PUT", endpoint="comment", data=data)

    def like(self, comment_id: int, score: int, private: bool | None = None, emoji: str | None = None) -> dict | None:
        """Vote on a comment.

        API endpoint: POST comment/like

        Args:
            comment_id (int): Comment id being voted on.
            score (int): 1 and -1 for up/down vote respectively. 0 to undo a vote.
            private (bool | None, optional): Should this vote be federated? Defaults to None.
            emoji (str | None, optional): Emoji reaction to include with vote if desired. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return self._client.request(method="POST", endpoint="comment/like", data=data)

    def save(self, comment_id: int, save: bool) -> dict | None:
        """Save a comment.

        API endpoint: PUT comment/save

        Args:
            comment_id (int): Comment id being saved.
            save (bool): True to save. False to remove from saved.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "save": save}

        return self._client.request(method="PUT", endpoint="comment/save", data=data)

    def subscribe(self, comment_id: int, subscribe: bool) -> dict | None:
        """Get notified of new replies to a comment.

        API endpoint: PUT comment/subscribe

        Args:
            comment_id (int): Comment id to subscribe to.
            subscribe (bool): True to subscribe. False to remove subscription.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="comment/subscribe", data=data)

    def delete(self, comment_id: int, deleted: bool) -> dict | None:
        """Delete a comment.

        API endpoint: POST comment/delete

        Args:
            comment_id (int): Comment id of the comment being deleted.
            deleted (bool): True to delete the comment. False to restore it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="comment/delete", data=data)

    def report(
        self,
        comment_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        """Report a comment to moderators/admins.

        API endpoint: POST comment/report

        Args:
            comment_id (int): Comment id to report.
            reason (str): Reason for the report.
            description (str | None, optional): Additional details to provide with the report. Defaults to None.
            report_remote (bool | None, optional): Forward report to the author's remote admins if applicable. Defaults
                to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """List comment reports.

        API endpoint: GET comment/report/list

        Args:
            comment_id (int | None, optional): Filter reports to a single comment by id. Defaults to None.
            community_id (int | None, optional): Filter reports to a single community by id. Defaults to None.
            limit (int | None, optional): Max number of reports per page. Defaults to None.
            page (int | None, optional): Page number to request. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Resolve a report.

        API endpoint: PUT comment/report/resolve

        Args:
            report_id (int): Report id that is being resolved (or unresolved).
            resolved (bool): True to resolve the report. False to unresolve it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return self._client.request(method="PUT", endpoint="comment/report/resolve", data=data)

    def remove(self, comment_id: int, removed: bool, reason: str | None = None) -> dict | None:
        """Remove a comment as a moderator/admin.

        API endpoint: POST comment/remove

        Args:
            comment_id (int): Comment id of the comment being removed.
            removed (bool): True to remove the comment. False to restore it.
            reason (str | None, optional): Reason for removal. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "removed": removed}

        if reason is not None:
            data["reason"] = reason

        return self._client.request(method="POST", endpoint="comment/remove", data=data)

    def mark_as_read(self, comment_reply_id: int, read: bool) -> dict | None:
        """Mark a comment as read or unread.

        API endpoint: POST comment/mark_as_read

        Args:
            comment_reply_id (int): Comment id being marked as read or unread.
            read (bool): True to mark as read. False to mark as unread.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_reply_id": comment_reply_id, "read": read}

        return self._client.request(method="POST", endpoint="comment/mark_as_read", data=data)

    def mark_as_answer(self, comment_reply_id: int, answer: bool) -> dict | None:
        """Mark a comment as an answer in a question and answer community.

        API endpoint: POST comment/mark_as_answer

        Args:
            comment_reply_id (int): Comment id being marked as an answer.
            answer (bool): True to mark it as an answer. False to unmark it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_reply_id": comment_reply_id, "answer": answer}

        return self._client.request(method="POST", endpoint="comment/mark_as_answer", data=data)

    def distinguish(self, comment_reply_id: int, distinguished: bool) -> dict | None:
        """Mark or unmark a comment as being spoken by a moderator.

        API endpoint: POST comment/distinguish

        Args:
            comment_reply_id (int): Comment id being distinguished.
            distinguished (bool): True to distinguish the comment. False to undistinguish it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_reply_id": comment_reply_id, "distinguished": distinguished}

        return self._client.request(method="POST", endpoint="comment/distinguish", data=data)

    def lock(self, comment_id: int, locked: bool) -> dict | None:
        """Lock a comment chain, preventing further replies.

        API endpoint: POST comment/lock

        Args:
            comment_id (int): Comment id of comment being locked.
            locked (bool): True to lock the comment. False to unlock it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "locked": locked}

        return self._client.request(method="POST", endpoint="comment/lock", data=data)

    def list_likes(self, comment_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        """List the votes on a comment.

        API endpoint: GET comment/like/list

        Args:
            comment_id (int): Comment id of the comment votes being fetched.
            page (int | None, optional): Page number of the results to fetch. Defaults to None.
            limit (int | None, optional): Max number of votes on each page of results. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get list of comments.

        API endpoint: GET comment/list

        Args:
            limit (int | None, optional): Max number to return for a page of results. Defaults to None.
            page (int | None, optional): Page of results to request. Defaults to None.
            sort (str | None, optional): Sorting method for the returned comments. Defaults to None.
            type_ (str | None, optional): Type filter (Subscribed, Local, etc.). Defaults to None.
            liked_only (bool | None, optional): Only return liked comments. Defaults to None.
            saved_only (bool | None, optional): Only return saved comments. Defaults to None.
            person_id (int | None, optional): Filter to comments by a specific user. Defaults to None.
            community_id (int | None, optional): Filter to comments in a specific community. Defaults to None.
            post_id (int | None, optional): Filter to comments on a specific post. Defaults to None.
            parent_id (int | None, optional): Filter to replies to a specific comment. Defaults to None.
            max_depth (int | None, optional): Max number of nested levels to return. Defaults to None.
            depth_first (bool | None, optional): Guarantee parent comments are on the same page as any fetched comments.
                Defaults to None.

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
        """Get info for a single comment.

        API endpoint: GET comment

        Args:
            comment_id (int): Comment id of the comment to retrieve.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="comment", params={"id": comment_id})

    async def create(
        self,
        body: str,
        post_id: int,
        parent_id: int | None = None,
        language_id: int | None = None,
    ) -> dict | None:
        """Create a comment.

        API endpoint: POST comment

        Args:
            body (str): Content of the comment in markdown.
            post_id (int): Post id that the comment is replying to.
            parent_id (int | None, optional): Parent comment id if the comment is a reply to another comment. Defaults
                to None.
            language_id (int | None, optional): Language id of the comment. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Edit a comment

        API endpoint: PUT comment

        Args:
            comment_id (int): The comment id of the comment to edit.
            body (str): New, edited content of the body in markdown.
            language_id (int | None, optional): Language id of the comment. Defaults to None.
            distinguished (bool | None, optional): Distinguish the comment as written by a moderator. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "body": body}

        if language_id is not None:
            data["language_id"] = language_id
        if distinguished is not None:
            data["distinguished"] = distinguished

        return await self._client.request(method="PUT", endpoint="comment", data=data)

    async def like(
        self, comment_id: int, score: int, private: bool | None = None, emoji: str | None = None
    ) -> dict | None:
        """Vote on a comment.

        API endpoint: POST comment/like

        Args:
            comment_id (int): Comment id being voted on.
            score (int): 1 and -1 for up/down vote respectively. 0 to undo a vote.
            private (bool | None, optional): Should this vote be federated? Defaults to None.
            emoji (str | None, optional): Emoji reaction to include with vote if desired. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return await self._client.request(method="POST", endpoint="comment/like", data=data)

    async def save(self, comment_id: int, save: bool) -> dict | None:
        """Save a comment.

        API endpoint: PUT comment/save

        Args:
            comment_id (int): Comment id being saved.
            save (bool): True to save. False to remove from saved.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "save": save}

        return await self._client.request(method="PUT", endpoint="comment/save", data=data)

    async def subscribe(self, comment_id: int, subscribe: bool) -> dict | None:
        """Get notified of new replies to a comment.

        API endpoint: PUT comment/subscribe

        Args:
            comment_id (int): Comment id to subscribe to.
            subscribe (bool): True to subscribe. False to remove subscription.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="comment/subscribe", data=data)

    async def delete(self, comment_id: int, deleted: bool) -> dict | None:
        """Delete a comment.

        API endpoint: POST comment/delete

        Args:
            comment_id (int): Comment id of the comment being deleted.
            deleted (bool): True to delete the comment. False to restore it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="comment/delete", data=data)

    async def report(
        self,
        comment_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        """Report a comment to moderators/admins.

        API endpoint: POST comment/report

        Args:
            comment_id (int): Comment id to report.
            reason (str): Reason for the report.
            description (str | None, optional): Additional details to provide with the report. Defaults to None.
            report_remote (bool | None, optional): Forward report to the author's remote admins if applicable. Defaults
                to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """List comment reports.

        API endpoint: GET comment/report/list

        Args:
            comment_id (int | None, optional): Filter reports to a single comment by id. Defaults to None.
            community_id (int | None, optional): Filter reports to a single community by id. Defaults to None.
            limit (int | None, optional): Max number of reports per page. Defaults to None.
            page (int | None, optional): Page number to request. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Resolve a report.

        API endpoint: PUT comment/report/resolve

        Args:
            report_id (int): Report id that is being resolved (or unresolved).
            resolved (bool): True to resolve the report. False to unresolve it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(method="PUT", endpoint="comment/report/resolve", data=data)

    async def remove(self, comment_id: int, removed: bool, reason: str | None = None) -> dict | None:
        """Remove a comment as a moderator/admin.

        API endpoint: POST comment/remove

        Args:
            comment_id (int): Comment id of the comment being removed.
            removed (bool): True to remove the comment. False to restore it.
            reason (str | None, optional): Reason for removal. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "removed": removed}

        if reason is not None:
            data["reason"] = reason

        return await self._client.request(method="POST", endpoint="comment/remove", data=data)

    async def mark_as_read(self, comment_reply_id: int, read: bool) -> dict | None:
        """Mark a comment as read or unread.

        API endpoint: POST comment/mark_as_read

        Args:
            comment_reply_id (int): Comment id being marked as read or unread.
            read (bool): True to mark as read. False to mark as unread.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_reply_id": comment_reply_id, "read": read}

        return await self._client.request(method="POST", endpoint="comment/mark_as_read", data=data)

    async def mark_as_answer(self, comment_reply_id: int, answer: bool) -> dict | None:
        """Mark a comment as an answer in a question and answer community.

        API endpoint: POST comment/mark_as_answer

        Args:
            comment_reply_id (int): Comment id being marked as an answer.
            answer (bool): True to mark it as an answer. False to unmark it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_reply_id": comment_reply_id, "answer": answer}

        return await self._client.request(method="POST", endpoint="comment/mark_as_answer", data=data)

    async def distinguish(self, comment_reply_id: int, distinguished: bool) -> dict | None:
        """Mark or unmark a comment as being spoken by a moderator.

        API endpoint: POST comment/distinguish

        Args:
            comment_reply_id (int): Comment id being distinguished.
            distinguished (bool): True to distinguish the comment. False to undistinguish it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_reply_id": comment_reply_id, "distinguished": distinguished}

        return await self._client.request(method="POST", endpoint="comment/distinguish", data=data)

    async def lock(self, comment_id: int, locked: bool) -> dict | None:
        """Lock a comment chain, preventing further replies.

        API endpoint: POST comment/lock

        Args:
            comment_id (int): Comment id of comment being locked.
            locked (bool): True to lock the comment. False to unlock it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"comment_id": comment_id, "locked": locked}

        return await self._client.request(method="POST", endpoint="comment/lock", data=data)

    async def list_likes(self, comment_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        """List the votes on a comment.

        API endpoint: GET comment/like/list

        Args:
            comment_id (int): Comment id of the comment votes being fetched.
            page (int | None, optional): Page number of the results to fetch. Defaults to None.
            limit (int | None, optional): Max number of votes on each page of results. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {"comment_id": comment_id}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="comment/like/list", params=params)
