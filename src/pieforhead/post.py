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
        """Get list of posts.

        API endpoint: GET post/list

        Args:
            query (str | None, optional): Text query to search. Defaults to None.
            sort (str | None, optional): Sorting method of returned posts. See PieFed API for more info. Defaults to
                None.
            type_ (str | None, optional): Different type filters. See PieFed API for more info. Defaults to None.
            community_name (str | None, optional): Restrict posts to one community by name. Defaults to None.
            community_id (int | None, optional): Restrict posts to one community by id. Defaults to None.
            saved_only (bool | None, optional): Only return saved posts. Defaults to None.
            nsfw (str | None, optional): How to include NSFW posts. Defaults to None.
            person_id (int | None, optional): Only return posts by one user by id. Defaults to None.
            limit (int | None, optional): Maximum posts returned on one page. Defaults to None.
            page (int | None, optional): Page number to fetch. Defaults to None.
            liked_only (bool | None, optional): Only return posts with upvotes. Defaults to None.
            feed_id (int | None, optional): Only return posts belonging to a feed by id. Defaults to None.
            topic_id (int | None, optional): Only return posts belonging to a topic by id. Defaults to None.
            ignore_sticky (bool | None, optional): Ignore sticky status when sorting results. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get list of scheduled posts.

        API endpoint: GET post/scheduled/list

        Args:
            query (str | None, optional): Text query to search. Defaults to None.
            sort (str | None, optional): Sorting method of returned posts. See PieFed API for more info. Defaults to
                None.
            community_name (str | None, optional): Restrict posts to one community by name. Defaults to None.
            community_id (int | None, optional): Restrict posts to one community by id. Defaults to None.
            include_deleted (bool | None, optional): Include deleted posts in the response. Defaults to None.
            limit (int | None, optional): Maximum number of posts to include in a page of results. Defaults to None.
            page (int | None, optional): Results page number to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get details for a single post.

        API endpoint: GET post

        Args:
            post_id (int): Post id of post to fetch.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Create a post.

        API endpoint: POST post

        Args:
            title (str): Title of the post.
            community_id (int): Community id for community to make the post in.
            alt_text (str | None, optional): Alt text to include for an image url post. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): URL to link to for the post. Defaults to None.
            og_image_url (str | None, optional): URL for a thumbnail for the post. Defaults to None.
            nsfw (bool | None, optional): True to mark the post as NSFW. Defaults to None.
            ai_generated (bool | None, optional): True to mark the post as AI generated. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        ai_generated: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        tags: str | None = None,
        flair: str | None = None,
    ) -> dict | None:
        """Edit a post.

        API endpoint: PUT post

        Args:
            post_id (int): Post id of the post to edit.
            alt_text (str | None, optional): Alt text to include for an image url post. Set to an empty string to
                remove. Defaults to None.
            title (str | None, optional): Title of the post. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): URL to link to for the post. Set to an empty string to remove. Defaults to None.
            nsfw (bool | None, optional): True to mark the post as NSFW. Defaults to None.
            ai_generated (bool | None, optional): True to mark the post as AI generated. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.
            tags (str | None, optional): Comma-separated list of hashtags without the # character. Set to an empty
                string to remove. Defaults to None.
            flair (str | None, optional): Comma-separated list of flair names. Set to an empty string to remove.
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id}

        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
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
        """Get a single scheduled post.

        API endpoint: GET post/scheduled

        Args:
            post_id (int): Post id of the scheduled post to fetch.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Create a scheduled post.

        API endpoint: POST post/scheduled

        Args:
            title (str): Title of the post. See PieFed's webUI when making a post to see details on templating format of
                scheduled posts.
            community_id (int): Community id of the community in which to make the post.
            scheduled_for (str): Datetime string for when to publish the post.
            alt_text (str | None, optional): Alt text to use for an image url post. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): Target url of the post. Defaults to None.
            og_image_url (str | None, optional): Optional thumbnail to use for the post. Defaults to None.
            nsfw (bool | None, optional): Mark the post as NSFW. Defaults to None.
            ai_generated (bool | None, optional): Mark the post as AI generated. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.
            repeat (str | None, optional): How often the post should repeat (None, Daily, etc.). See PieFed API for more
                info. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Edit a scheduled post.

        API endpoint: PUT post/scheduled

        Args:
            post_id (int): The post id of the scheduled post being edited.
            alt_text (str | None, optional): Alt text to use for an image url post. Defaults to None.
            title (str | None, optional): Title of the post. See PieFed's webUI when making a post to see details on
                templating format of scheduled posts. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): Target url of the post. Defaults to None.
            nsfw (bool | None, optional): Mark the post as NSFW. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.
            tags (str | None, optional): Comma-separated list of hashtags without the # character. Set to an empty
                string to remove. Defaults to None.
            flair (str | None, optional): Comma-separated list of flair names. Set to an empty string to remove.
                Defaults to None.
            scheduled_for (str | None, optional): Datetime string for when to publish the post. Defaults to None.
            repeat (str | None, optional): How often the post should repeat (None, Daily, etc.). See PieFed API for more
                info. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get replies to a post with a nested structure.

        API endpoint: GET post/replies

        Args:
            post_id (int | None, optional): Post id of the post whose comments are being fetched. Defaults to None.
            parent_id (int | None, optional): Comment id if fetching replies to an individual comment. Defaults to None.
            sort (str | None, optional): Sort method to return results with. See the PieFed API docs for options.
                Defaults to None.
            max_depth (int | None, optional): Max number of nested levels to fetch. Defaults to None.
            page (str | None, optional): Page number of results to get. Defaults to None.
            limit (int | None, optional): Max number of top-level items to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Fetch the metadata of a url that can be used to generate a post title/body/thumbnail.

        API endpoint: GET post/site_metadata

        Args:
            url (str): URL to fetch metadata for.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="GET", endpoint="post/site_metadata", params={"url": url})

    def like(self, post_id: int, score: int, private: bool | None = None, emoji: str | None = None) -> dict | None:
        """Vote on a post.

        API endpoint: POST post/like

        Args:
            post_id (int): Post id of post being voted on.
            score (int): +/- 1 for up/down vote. 0 to undo vote.
            private (bool | None, optional): Should the vote be federated. Defaults to None.
            emoji (str | None, optional): Emoji reaction to accompany vote. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return self._client.request(method="POST", endpoint="post/like", data=data)

    def save(self, post_id: int, save: bool) -> dict | None:
        """Save a post.

        API endpoint: PUT post/save

        Args:
            post_id (int): Post id to save.
            save (bool): True to save. False to unsave.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="PUT", endpoint="post/save", data={"post_id": post_id, "save": save})

    def subscribe(self, post_id: int, subscribe: bool) -> dict | None:
        """Get notified of new replies to a post.

        API endpoint: PUT post/subscribe

        Args:
            post_id (int): Post id of post to subscribe to.
            subscribe (bool): True to subscribe. False to unsubscribe.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="post/subscribe", data=data)

    def delete(self, post_id: int, deleted: bool) -> dict | None:
        """Delete a post.

        API endpoint: POST post/scheduled/delete

        Args:
            post_id (int): Post id of post to delete.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="post/delete", data=data)

    def delete_scheduled(self, post_id: int, deleted: bool) -> dict | None:
        """Delete a scheduled post.

        API endpoint: POST post/scheduled/delete

        Args:
            post_id (int): Post id of the post to delete.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="post/scheduled/delete", data=data)

    def report(
        self,
        post_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        """Report a post.

        API endpoint: POST post/report

        Args:
            post_id (int): Post id being reported.
            reason (str): Reason for report.
            description (str | None, optional): Additional info to include with report. Defaults to None.
            report_remote (bool | None, optional): Forward report on to the author's remote admins (if applicable).
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get list of reports.

        API endpoint: GET post/report/list

        Args:
            community_id (int | None, optional): Filter reports to a single community. Defaults to None.
            limit (int | None, optional): Max number of reports per page of results. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            post_id (int | None, optional): Filter reports to a single post. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Mark a report as resolved.

        API endpoint: PUT post/report/resolve

        Args:
            report_id (int): Report id of the report being resolved.
            resolved (bool): True to resolve. False to un-resolve.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return self._client.request(method="PUT", endpoint="post/report/resolve", data=data)

    def lock(self, post_id: int, locked: bool) -> dict | None:
        """Lock a post.

        API endpoint: POST post/lock

        Args:
            post_id (int): Post id of post being locked.
            locked (bool): True to lock post. False to unlock.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="POST", endpoint="post/lock", data={"post_id": post_id, "locked": locked})

    def hide(self, post_id: int, hidden: bool) -> dict | None:
        """Hide a post.

        API endpoint: POST post/hide

        Args:
            post_id (int): Post ide of post being hidden.
            hidden (bool): True to hide. False to un-hide.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return self._client.request(method="POST", endpoint="post/hide", data={"post_id": post_id, "hidden": hidden})

    def feature(self, post_id: int, featured: bool, feature_type: str | None = None) -> dict | None:
        """Feature (pin) a post.

        API endpoint: POST post/feature

        Args:
            post_id (int): Post id of post being pinned.
            featured (bool): True to feature. False to un-feature.
            feature_type (str | None, optional): Type of pin to do (Community or Local). Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "featured": featured}

        if feature_type is not None:
            data["feature_type"] = feature_type

        return self._client.request(method="POST", endpoint="post/feature", data=data)

    def remove(self, post_id: int, removed: bool, reason: str | None = None) -> dict | None:
        """Remove a post (as a moderator).

        API endpoint: POST post/remove

        Args:
            post_id (int): Post id of post being removed.
            removed (bool): True to remove. False to restore.
            reason (str | None, optional): Reason for removal. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Mark a post as read.

        API endpoint: POST post/mark_as_read

        Args:
            read (bool): True to mark as read. False to mark as unread.
            post_id (int | None, optional): Post id of individual post. Defaults to None.
            post_ids (list[int] | None, optional): List of multiple post ids. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"read": read}

        if post_id is not None:
            data["post_id"] = post_id
        if post_ids is not None:
            data["post_ids"] = post_ids

        return self._client.request(method="POST", endpoint="post/mark_as_read", data=data)

    def list_likes(self, post_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        """Get list of votes on a post.

        API endpoint: GET post/like/list

        Args:
            post_id (int): Post id of the post in question.
            page (int | None, optional): Page number of results to fetch. Defaults to None.
            limit (int | None, optional): Max number of results per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {"post_id": post_id}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return self._client.request(method="GET", endpoint="post/like/list", params=params)

    def assign_flair(self, post_id: int, flair_id_list: list[int] | None = None) -> dict | None:
        """Assign or remove flair from a post.

        API endpoint: POST post/assign_flair

        Args:
            post_id (int): Post id having its flair modified.
            flair_id_list (list[int] | None, optional): List of id flair that post should have. Set to an empty list to
                remove. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id}

        if flair_id_list is not None and flair_id_list != []:
            data["flair_id_list"] = flair_id_list
        elif flair_id_list == []:
            data["flair_id_list"] = None

        return self._client.request(method="POST", endpoint="post/assign_flair", data=data)

    def poll_vote(self, post_id: int, choice_id: list[int]) -> dict | None:
        """Vote on a poll post.

        API endpoint: POST post/poll_vote

        Args:
            post_id (int): Post id for which a vote is being cast.
            choice_id (list[int]): List of poll choice ids to vote for. For polls where only a single vote is allowed,
                must be length 1.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get list of posts.

        API endpoint: GET post/list

        Args:
            query (str | None, optional): Text query to search. Defaults to None.
            sort (str | None, optional): Sorting method of returned posts. See PieFed API for more info. Defaults to
                None.
            type_ (str | None, optional): Different type filters. See PieFed API for more info. Defaults to None.
            community_name (str | None, optional): Restrict posts to one community by name. Defaults to None.
            community_id (int | None, optional): Restrict posts to one community by id. Defaults to None.
            saved_only (bool | None, optional): Only return saved posts. Defaults to None.
            nsfw (str | None, optional): How to include NSFW posts. Defaults to None.
            person_id (int | None, optional): Only return posts by one user by id. Defaults to None.
            limit (int | None, optional): Maximum posts returned on one page. Defaults to None.
            page (int | None, optional): Page number to fetch. Defaults to None.
            liked_only (bool | None, optional): Only return posts with upvotes. Defaults to None.
            feed_id (int | None, optional): Only return posts belonging to a feed by id. Defaults to None.
            topic_id (int | None, optional): Only return posts belonging to a topic by id. Defaults to None.
            ignore_sticky (bool | None, optional): Ignore sticky status when sorting results. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get list of scheduled posts.

        API endpoint: GET post/scheduled/list

        Args:
            query (str | None, optional): Text query to search. Defaults to None.
            sort (str | None, optional): Sorting method of returned posts. See PieFed API for more info. Defaults to
                None.
            community_name (str | None, optional): Restrict posts to one community by name. Defaults to None.
            community_id (int | None, optional): Restrict posts to one community by id. Defaults to None.
            include_deleted (bool | None, optional): Include deleted posts in the response. Defaults to None.
            limit (int | None, optional): Maximum number of posts to include in a page of results. Defaults to None.
            page (int | None, optional): Results page number to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get details for a single post.

        API endpoint: GET post

        Args:
            post_id (int): Post id of post to fetch.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Create a post.

        API endpoint: POST post

        Args:
            title (str): Title of the post.
            community_id (int): Community id for community to make the post in.
            alt_text (str | None, optional): Alt text to include for an image url post. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): URL to link to for the post. Defaults to None.
            og_image_url (str | None, optional): URL for a thumbnail for the post. Defaults to None.
            nsfw (bool | None, optional): True to mark the post as NSFW. Defaults to None.
            ai_generated (bool | None, optional): True to mark the post as AI generated. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        ai_generated: bool | None = None,
        language_id: int | None = None,
        event: dict | None = None,
        poll: dict | None = None,
        tags: str | None = None,
        flair: str | None = None,
    ) -> dict | None:
        """Edit a post.

        API endpoint: PUT post

        Args:
            post_id (int): Post id of the post to edit.
            alt_text (str | None, optional): Alt text to include for an image url post. Set to an empty string to
                remove. Defaults to None.
            title (str | None, optional): Title of the post. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): URL to link to for the post. Set to an empty string to remove. Defaults to None.
            nsfw (bool | None, optional): True to mark the post as NSFW. Defaults to None.
            ai_generated (bool | None, optional): True to mark the post as AI generated. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.
            tags (str | None, optional): Comma-separated list of hashtags without the # character. Set to an empty
                string to remove. Defaults to None.
            flair (str | None, optional): Comma-separated list of flair names. Set to an empty string to remove.
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id}

        if title is not None:
            data["title"] = title
        if body is not None:
            data["body"] = body
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
        """Get a single scheduled post.

        API endpoint: GET post/scheduled

        Args:
            post_id (int): Post id of the scheduled post to fetch.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Create a scheduled post.

        API endpoint: POST post/scheduled

        Args:
            title (str): Title of the post. See PieFed's webUI when making a post to see details on templating format of
                scheduled posts.
            community_id (int): Community id of the community in which to make the post.
            scheduled_for (str): Datetime string for when to publish the post.
            alt_text (str | None, optional): Alt text to use for an image url post. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): Target url of the post. Defaults to None.
            og_image_url (str | None, optional): Optional thumbnail to use for the post. Defaults to None.
            nsfw (bool | None, optional): Mark the post as NSFW. Defaults to None.
            ai_generated (bool | None, optional): Mark the post as AI generated. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.
            repeat (str | None, optional): How often the post should repeat (None, Daily, etc.). See PieFed API for more
                info. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Edit a scheduled post.

        API endpoint: PUT post/scheduled

        Args:
            post_id (int): The post id of the scheduled post being edited.
            alt_text (str | None, optional): Alt text to use for an image url post. Defaults to None.
            title (str | None, optional): Title of the post. See PieFed's webUI when making a post to see details on
                templating format of scheduled posts. Defaults to None.
            body (str | None, optional): Body of the post in markdown. Defaults to None.
            url (str | None, optional): Target url of the post. Defaults to None.
            nsfw (bool | None, optional): Mark the post as NSFW. Defaults to None.
            language_id (int | None, optional): Language id of the post. Defaults to None.
            event (dict | None, optional): dict containing the event information. See the PieFed API for more
                information. Defaults to None.
            poll (dict | None, optional): dict containing the poll information. See the PieFed API for more information.
                Defaults to None.
            tags (str | None, optional): Comma-separated list of hashtags without the # character. Set to an empty
                string to remove. Defaults to None.
            flair (str | None, optional): Comma-separated list of flair names. Set to an empty string to remove.
                Defaults to None.
            scheduled_for (str | None, optional): Datetime string for when to publish the post. Defaults to None.
            repeat (str | None, optional): How often the post should repeat (None, Daily, etc.). See PieFed API for more
                info. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get replies to a post with a nested structure.

        API endpoint: GET post/replies

        Args:
            post_id (int | None, optional): Post id of the post whose comments are being fetched. Defaults to None.
            parent_id (int | None, optional): Comment id if fetching replies to an individual comment. Defaults to None.
            sort (str | None, optional): Sort method to return results with. See the PieFed API docs for options.
                Defaults to None.
            max_depth (int | None, optional): Max number of nested levels to fetch. Defaults to None.
            page (str | None, optional): Page number of results to get. Defaults to None.
            limit (int | None, optional): Max number of top-level items to fetch. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Fetch the metadata of a url that can be used to generate a post title/body/thumbnail.

        API endpoint: GET post/site_metadata

        Args:
            url (str): URL to fetch metadata for.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="GET", endpoint="post/site_metadata", params={"url": url})

    async def like(
        self,
        post_id: int,
        score: int,
        private: bool | None = None,
        emoji: str | None = None,
    ) -> dict | None:
        """Vote on a post.

        API endpoint: POST post/like

        Args:
            post_id (int): Post id of post being voted on.
            score (int): +/- 1 for up/down vote. 0 to undo vote.
            private (bool | None, optional): Should the vote be federated. Defaults to None.
            emoji (str | None, optional): Emoji reaction to accompany vote. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "score": score}

        if private is not None:
            data["private"] = private
        if emoji is not None:
            data["emoji"] = emoji

        return await self._client.request(method="POST", endpoint="post/like", data=data)

    async def save(self, post_id: int, save: bool) -> dict | None:
        """Save a post.

        API endpoint: PUT post/save

        Args:
            post_id (int): Post id to save.
            save (bool): True to save. False to unsave.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(method="PUT", endpoint="post/save", data={"post_id": post_id, "save": save})

    async def subscribe(self, post_id: int, subscribe: bool) -> dict | None:
        """Get notified of new replies to a post.

        API endpoint: PUT post/subscribe

        Args:
            post_id (int): Post id of post to subscribe to.
            subscribe (bool): True to subscribe. False to unsubscribe.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="post/subscribe", data=data)

    async def delete(self, post_id: int, deleted: bool) -> dict | None:
        """Delete a post.

        API endpoint: POST post/scheduled/delete

        Args:
            post_id (int): Post id of post to delete.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="post/delete", data=data)

    async def delete_scheduled(self, post_id: int, deleted: bool) -> dict | None:
        """Delete a scheduled post.

        API endpoint: POST post/scheduled/delete

        Args:
            post_id (int): Post id of the post to delete.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="post/scheduled/delete", data=data)

    async def report(
        self,
        post_id: int,
        reason: str,
        description: str | None = None,
        report_remote: bool | None = None,
    ) -> dict | None:
        """Report a post.

        API endpoint: POST post/report

        Args:
            post_id (int): Post id being reported.
            reason (str): Reason for report.
            description (str | None, optional): Additional info to include with report. Defaults to None.
            report_remote (bool | None, optional): Forward report on to the author's remote admins (if applicable).
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Get list of reports.

        API endpoint: GET post/report/list

        Args:
            community_id (int | None, optional): Filter reports to a single community. Defaults to None.
            limit (int | None, optional): Max number of reports per page of results. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            post_id (int | None, optional): Filter reports to a single post. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Mark a report as resolved.

        API endpoint: PUT post/report/resolve

        Args:
            report_id (int): Report id of the report being resolved.
            resolved (bool): True to resolve. False to un-resolve.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(method="PUT", endpoint="post/report/resolve", data=data)

    async def lock(self, post_id: int, locked: bool) -> dict | None:
        """Lock a post.

        API endpoint: POST post/lock

        Args:
            post_id (int): Post id of post being locked.
            locked (bool): True to lock post. False to unlock.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        return await self._client.request(
            method="POST",
            endpoint="post/lock",
            data={"post_id": post_id, "locked": locked},
        )

    async def hide(self, post_id: int, hidden: bool) -> dict | None:
        """Hide a post.

        API endpoint: POST post/hide

        Args:
            post_id (int): Post ide of post being hidden.
            hidden (bool): True to hide. False to un-hide.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "hidden": hidden}

        return await self._client.request(method="POST", endpoint="post/hide", data=data)

    async def feature(self, post_id: int, featured: bool, feature_type: str | None = None) -> dict | None:
        """Feature (pin) a post.

        API endpoint: POST post/feature

        Args:
            post_id (int): Post id of post being pinned.
            featured (bool): True to feature. False to un-feature.
            feature_type (str | None, optional): Type of pin to do (Community or Local). Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "featured": featured}

        if feature_type is not None:
            data["feature_type"] = feature_type

        return await self._client.request(method="POST", endpoint="post/feature", data=data)

    async def remove(self, post_id: int, removed: bool, reason: str | None = None) -> dict | None:
        """Remove a post (as a moderator).

        API endpoint: POST post/remove

        Args:
            post_id (int): Post id of post being removed.
            removed (bool): True to remove. False to restore.
            reason (str | None, optional): Reason for removal. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
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
        """Mark a post as read.

        API endpoint: POST post/mark_as_read

        Args:
            read (bool): True to mark as read. False to mark as unread.
            post_id (int | None, optional): Post id of individual post. Defaults to None.
            post_ids (list[int] | None, optional): List of multiple post ids. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"read": read}

        if post_id is not None:
            data["post_id"] = post_id
        if post_ids is not None:
            data["post_ids"] = post_ids

        return await self._client.request(method="POST", endpoint="post/mark_as_read", data=data)

    async def list_likes(self, post_id: int, page: int | None = None, limit: int | None = None) -> dict | None:
        """Get list of votes on a post.

        API endpoint: GET post/like/list

        Args:
            post_id (int): Post id of the post in question.
            page (int | None, optional): Page number of results to fetch. Defaults to None.
            limit (int | None, optional): Max number of results per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {"post_id": post_id}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="post/like/list", params=params)

    async def assign_flair(self, post_id: int, flair_id_list: list[int] | None = None) -> dict | None:
        """Assign or remove flair from a post.

        API endpoint: POST post/assign_flair

        Args:
            post_id (int): Post id having its flair modified.
            flair_id_list (list[int] | None, optional): List of id flair that post should have. Set to an empty list to
                remove. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id}

        if flair_id_list is not None and flair_id_list != []:
            data["flair_id_list"] = flair_id_list
        elif flair_id_list == []:
            data["flair_id_list"] = None

        return await self._client.request(method="POST", endpoint="post/assign_flair", data=data)

    async def poll_vote(self, post_id: int, choice_id: list[int]) -> dict | None:
        """Vote on a poll post.

        API endpoint: POST post/poll_vote

        Args:
            post_id (int): Post id for which a vote is being cast.
            choice_id (list[int]): List of poll choice ids to vote for. For polls where only a single vote is allowed,
                must be length 1.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"post_id": post_id, "choice_id": choice_id}

        return await self._client.request(method="POST", endpoint="post/poll_vote", data=data)
