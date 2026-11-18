from .clients import PieFedClient, AsyncPieFedClient


class PrivateMessage:
    """Class to hold private message endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list_messages(
        self, page: int | None = None, limit: int | None = None, unread_only: bool | None = None
    ) -> dict | None:
        """Get list of private messages.

        API endpoint: GET private_message/list

        Args:
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.
            unread_only (bool | None, optional): Only return unread private messages. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if unread_only is not None:
            params["unread_only"] = unread_only

        return self._client.request(method="GET", endpoint="private_message/list", params=params)

    def get_conversation(
        self,
        person_id: int | None = None,
        conversation_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict | None:
        """Get the messages in a specific conversation.

        API endpoint: GET private_message/conversation

        Args:
            person_id (int | None, optional): User id that the conversation is with. Defaults to None.
            conversation_id (int | None, optional): Conversation id of the conversation to fetch. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if person_id is not None:
            params["person_id"] = person_id
        if conversation_id is not None:
            params["conversation_id"] = conversation_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return self._client.request(method="GET", endpoint="private_message/conversation", params=params)

    def leave_conversation(self, conversation_id: int) -> bool | None:
        """Leave a conversation.

        API endpoint: POST private_message/conversation/leave

        Args:
            conversation_id (int): Conversation id of conversation to leave.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"conversation_id": conversation_id}

        return self._client.request(method="POST", endpoint="private_message/conversation/leave", data=data)

    def create(self, content: str, recipient_id: int) -> dict | None:
        """Create a private message.

        API endpoint: POST private_message

        Args:
            content (str): Message body in markdown.
            recipient_id (int): User id to send message to.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"content": content, "recipient_id": recipient_id}

        return self._client.request(method="POST", endpoint="private_message", data=data)

    def edit(self, content: str, private_message_id: int) -> dict | None:
        """Edit a private message.

        API endpoint: PUT private_message

        Args:
            content (str): New content of the private message in markdown.
            private_message_id (int): Id of the private message to edit.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "content": content}

        return self._client.request(method="PUT", endpoint="private_message", data=data)

    def mark_as_read(self, private_message_id: int, read: bool) -> dict | None:
        """Mark a private message as read.

        API endpoint: POST private_message/mark_as_read

        Args:
            private_message_id (int): Id of the private message to mark as read.
            read (bool): True to mark as read. False to mark as unread.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "read": read}

        return self._client.request(method="POST", endpoint="private_message/mark_as_read", data=data)

    def delete(self, private_message_id: int, deleted: bool) -> dict | None:
        """Delete a private message.

        API endpoint: POST private_message/delete

        Args:
            private_message_id (int): Id of the private message to delete.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="private_message/delete", data=data)

    def report(self, private_message_id: int, reason: str) -> dict | None:
        """Report a private message.

        API endpoint: POST private_message/report

        Args:
            private_message_id (int): Id of the private message to report.
            reason (str): Reason for the report.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "reason": reason}

        return self._client.request(method="POST", endpoint="private_message/report", data=data)

    def report_conversation(self, conversation_id: int, reason: str) -> bool | None:
        """Report a whole conversation.

        API endpoint: POST private_message/conversation/report

        Args:
            conversation_id (int): Id of the conversation to report.
            reason (str): Reason for the report.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"conversation_id": conversation_id, "reason": reason}

        return self._client.request(method="POST", endpoint="private_message/conversation/report", data=data)

    def list_reports(
        self,
        conversation_id: int | None = None,
        private_message_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        unresolved_only: bool | None = None,
    ) -> dict | None:
        """Get list of private message reports.

        API endpoint: GET private_message/repor/list

        Args:
            conversation_id (int | None, optional): Limit reports to a single conversation. Defaults to None.
            private_message_id (int | None, optional): Fetch reports for just a single private message. Defaults to
                None.
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if conversation_id is not None:
            params["conversation_id"] = conversation_id
        if private_message_id is not None:
            params["private_message_id"] = private_message_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only

        return self._client.request(method="GET", endpoint="private_message/report/list", params=params)

    def list_conversation_reports(
        self,
        conversation_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        unresolved_only: bool | None = None,
        message_history_limit: int | None = None,
    ) -> dict | None:
        """Get reports for a conversation.

        API endpoint: GET private_message/conversation/report/list

        Args:
            conversation_id (int | None, optional): Limit results to just a single conversation. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.
            message_history_limit (int | None, optional): Max number of most recent messages in conversation to return.
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if conversation_id is not None:
            params["conversation_id"] = conversation_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only
        if message_history_limit is not None:
            params["message_history_limit"] = message_history_limit

        return self._client.request(method="GET", endpoint="private_message/conversation/report/list", params=params)

    def resolve_report(self, report_id: int, resolved: bool) -> dict | None:
        """Resolve a private message report.

        API endpoint: PUT private_message/report/resolve

        Args:
            report_id (int): Report id of the report in question.
            resolved (bool): True to resolve. False to un-resolve.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return self._client.request(method="PUT", endpoint="private_message/report/resolve", data=data)

    def resolve_conversation_report(self, report_id: int, resolved: bool) -> bool | None:
        """Resolve a conversation report.

        API endpoint: PUT private_message/conversation/report/resolve

        Args:
            report_id (int): Report id of the report in question.
            resolved (bool): True to resolve. False to un-resolve.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return self._client.request(method="PUT", endpoint="private_message/conversation/report/resolve", data=data)


class PrivateMessageAsync:
    """Class to hold async private message endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def list_messages(
        self,
        page: int | None = None,
        limit: int | None = None,
        unread_only: bool | None = None,
    ) -> dict | None:
        """Get list of private messages.

        API endpoint: GET private_message/list

        Args:
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.
            unread_only (bool | None, optional): Only return unread private messages. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if unread_only is not None:
            params["unread_only"] = unread_only

        return await self._client.request(method="GET", endpoint="private_message/list", params=params)

    async def get_conversation(
        self,
        person_id: int | None = None,
        conversation_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict | None:
        """Get the messages in a specific conversation.

        API endpoint: GET private_message/conversation

        Args:
            person_id (int | None, optional): User id that the conversation is with. Defaults to None.
            conversation_id (int | None, optional): Conversation id of the conversation to fetch. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if person_id is not None:
            params["person_id"] = person_id
        if conversation_id is not None:
            params["conversation_id"] = conversation_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        return await self._client.request(method="GET", endpoint="private_message/conversation", params=params)

    async def leave_conversation(self, conversation_id: int) -> bool | None:
        """Leave a conversation.

        API endpoint: POST private_message/conversation/leave

        Args:
            conversation_id (int): Conversation id of conversation to leave.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"conversation_id": conversation_id}

        return await self._client.request(method="POST", endpoint="private_message/conversation/leave", data=data)

    async def create(self, content: str, recipient_id: int) -> dict | None:
        """Create a private message.

        API endpoint: POST private_message

        Args:
            content (str): Message body in markdown.
            recipient_id (int): User id to send message to.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"content": content, "recipient_id": recipient_id}

        return await self._client.request(method="POST", endpoint="private_message", data=data)

    async def edit(self, content: str, private_message_id: int) -> dict | None:
        """Edit a private message.

        API endpoint: PUT private_message

        Args:
            content (str): New content of the private message in markdown.
            private_message_id (int): Id of the private message to edit.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "content": content}

        return await self._client.request(method="PUT", endpoint="private_message", data=data)

    async def mark_as_read(self, private_message_id: int, read: bool) -> dict | None:
        """Mark a private message as read.

        API endpoint: POST private_message/mark_as_read

        Args:
            private_message_id (int): Id of the private message to mark as read.
            read (bool): True to mark as read. False to mark as unread.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "read": read}

        return await self._client.request(method="POST", endpoint="private_message/mark_as_read", data=data)

    async def delete(self, private_message_id: int, deleted: bool) -> dict | None:
        """Delete a private message.

        API endpoint: POST private_message/delete

        Args:
            private_message_id (int): Id of the private message to delete.
            deleted (bool): True to delete. False to restore.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="private_message/delete", data=data)

    async def report(self, private_message_id: int, reason: str) -> dict | None:
        """Report a private message.

        API endpoint: POST private_message/report

        Args:
            private_message_id (int): Id of the private message to report.
            reason (str): Reason for the report.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"private_message_id": private_message_id, "reason": reason}

        return await self._client.request(method="POST", endpoint="private_message/report", data=data)

    async def report_conversation(self, conversation_id: int, reason: str) -> bool | None:
        """Report a whole conversation.

        API endpoint: POST private_message/conversation/report

        Args:
            conversation_id (int): Id of the conversation to report.
            reason (str): Reason for the report.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"conversation_id": conversation_id, "reason": reason}

        return await self._client.request(
            method="POST",
            endpoint="private_message/conversation/report",
            data=data,
        )

    async def list_reports(
        self,
        conversation_id: int | None = None,
        private_message_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        unresolved_only: bool | None = None,
    ) -> dict | None:
        """Get list of private message reports.

        API endpoint: GET private_message/repor/list

        Args:
            conversation_id (int | None, optional): Limit reports to a single conversation. Defaults to None.
            private_message_id (int | None, optional): Fetch reports for just a single private message. Defaults to
                None.
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if conversation_id is not None:
            params["conversation_id"] = conversation_id
        if private_message_id is not None:
            params["private_message_id"] = private_message_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only

        return await self._client.request(method="GET", endpoint="private_message/report/list", params=params)

    async def list_conversation_reports(
        self,
        conversation_id: int | None = None,
        limit: int | None = None,
        page: int | None = None,
        unresolved_only: bool | None = None,
        message_history_limit: int | None = None,
    ) -> dict | None:
        """Get reports for a conversation.

        API endpoint: GET private_message/conversation/report/list

        Args:
            conversation_id (int | None, optional): Limit results to just a single conversation. Defaults to None.
            limit (int | None, optional): Max results per page. Defaults to None.
            page (int | None, optional): Page of results to fetch. Defaults to None.
            unresolved_only (bool | None, optional): Only return unresolved reports. Defaults to None.
            message_history_limit (int | None, optional): Max number of most recent messages in conversation to return.
                Defaults to None.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        params = {}

        if conversation_id is not None:
            params["conversation_id"] = conversation_id
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if unresolved_only is not None:
            params["unresolved_only"] = unresolved_only
        if message_history_limit is not None:
            params["message_history_limit"] = message_history_limit

        return await self._client.request(
            method="GET",
            endpoint="private_message/conversation/report/list",
            params=params,
        )

    async def resolve_report(self, report_id: int, resolved: bool) -> dict | None:
        """Resolve a private message report.

        API endpoint: PUT private_message/report/resolve

        Args:
            report_id (int): Report id of the report in question.
            resolved (bool): True to resolve. False to un-resolve.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(method="PUT", endpoint="private_message/report/resolve", data=data)

    async def resolve_conversation_report(self, report_id: int, resolved: bool) -> bool | None:
        """Resolve a conversation report.

        API endpoint: PUT private_message/conversation/report/resolve

        Args:
            report_id (int): Report id of the report in question.
            resolved (bool): True to resolve. False to un-resolve.

        Returns:
            bool | None: True if a successful network request. None is returned if an exception was raised and then
                subsequently ignored.
        """
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(
            method="PUT",
            endpoint="private_message/conversation/report/resolve",
            data=data,
        )
