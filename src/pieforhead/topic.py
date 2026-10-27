from .clients import PieFedClient, AsyncPieFedClient


class Topic:
    """Class to hold Topic endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list(self, include_communities: bool = True) -> dict | None:
        resp = self._client.request(
            method="GET",
            endpoint="topic/list",
            params={"include_communities": include_communities},
        )

        return resp


class TopicAsync:
    """Class to hold async Topic endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def list(self, include_communities: bool = True):
        resp = await self._client.request(
            method="GET",
            endpoint="topic/list",
            params={"include_communities": include_communities},
        )

        return resp
