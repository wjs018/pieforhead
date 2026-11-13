from .clients import PieFedClient, AsyncPieFedClient


class PrivateMessage:
    """Class to hold private message endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list_messages(
        self, page: int | None = None, limit: int | None = None, unread_only: bool | None = None
    ) -> dict | None:
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
        data = {"conversation_id": conversation_id}

        return self._client.request(method="POST", endpoint="private_message/conversation/leave", data=data)

    def create(self, content: str, recipient_id: int) -> dict | None:
        data = {"content": content, "recipient_id": recipient_id}

        return self._client.request(method="POST", endpoint="private_message", data=data)

    def edit(self, content: str, private_message_id: int) -> dict | None:
        data = {"private_message_id": private_message_id, "content": content}

        return self._client.request(method="PUT", endpoint="private_message", data=data)

    def mark_as_read(self, private_message_id: int, read: bool) -> dict | None:
        data = {"private_message_id": private_message_id, "read": read}

        return self._client.request(method="POST", endpoint="private_message/mark_as_read", data=data)

    def delete(self, private_message_id: int, deleted: bool) -> dict | None:
        data = {"private_message_id": private_message_id, "deleted": deleted}

        return self._client.request(method="POST", endpoint="private_message/delete", data=data)

    def report(self, private_message_id: int, reason: str) -> dict | None:
        data = {"private_message_id": private_message_id, "reason": reason}

        return self._client.request(method="POST", endpoint="private_message/report", data=data)

    def report_conversation(self, conversation_id: int, reason: str) -> bool | None:
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
        data = {"report_id": report_id, "resolved": resolved}

        return self._client.request(method="PUT", endpoint="private_message/report/resolve", data=data)

    def resolve_conversation_report(self, report_id: int, resolved: bool) -> bool | None:
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
        data = {"conversation_id": conversation_id}

        return await self._client.request(method="POST", endpoint="private_message/conversation/leave", data=data)

    async def create(self, content: str, recipient_id: int) -> dict | None:
        data = {"content": content, "recipient_id": recipient_id}

        return await self._client.request(method="POST", endpoint="private_message", data=data)

    async def edit(self, content: str, private_message_id: int) -> dict | None:
        data = {"private_message_id": private_message_id, "content": content}

        return await self._client.request(method="PUT", endpoint="private_message", data=data)

    async def mark_as_read(self, private_message_id: int, read: bool) -> dict | None:
        data = {"private_message_id": private_message_id, "read": read}

        return await self._client.request(method="POST", endpoint="private_message/mark_as_read", data=data)

    async def delete(self, private_message_id: int, deleted: bool) -> dict | None:
        data = {"private_message_id": private_message_id, "deleted": deleted}

        return await self._client.request(method="POST", endpoint="private_message/delete", data=data)

    async def report(self, private_message_id: int, reason: str) -> dict | None:
        data = {"private_message_id": private_message_id, "reason": reason}

        return await self._client.request(method="POST", endpoint="private_message/report", data=data)

    async def report_conversation(self, conversation_id: int, reason: str) -> bool | None:
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
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(method="PUT", endpoint="private_message/report/resolve", data=data)

    async def resolve_conversation_report(self, report_id: int, resolved: bool) -> bool | None:
        data = {"report_id": report_id, "resolved": resolved}

        return await self._client.request(
            method="PUT",
            endpoint="private_message/conversation/report/resolve",
            data=data,
        )
