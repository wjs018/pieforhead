from .clients import PieFedClient, AsyncPieFedClient


class Topic:
    """Class to hold Topic endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def list_topics(self, include_communities: bool = True) -> dict | None:
        """Get a list of topics on the instance.

        API endpoint: GET topic/list

        Args:
            include_communities (bool, optional): Include the communities of the topics in the response. Defaults to
                True.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        resp = self._client.request(
            method="GET",
            endpoint="topic/list",
            params={"include_communities": include_communities},
        )

        return resp

    def subscribe(self, topic_id: int, subscribe: bool) -> dict | None:
        """Get notified of new posts in a topic.

        API endpoint: PUT topic/subscribe

        Args:
            topic_id (int): Topic id to get notifications for.
            subscribe (bool): True to create activity alert. False to remove it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"topic_id": topic_id, "subscribe": subscribe}

        return self._client.request(method="PUT", endpoint="topic/subscribe", data=data)


class TopicAsync:
    """Class to hold async Topic endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def list_topics(self, include_communities: bool = True) -> dict | None:
        """Get a list of topics on the instance.

        API endpoint: GET topic/list

        Args:
            include_communities (bool, optional): Include the communities of the topics in the response. Defaults to
                True.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        resp = await self._client.request(
            method="GET",
            endpoint="topic/list",
            params={"include_communities": include_communities},
        )

        return resp

    async def subscribe(self, topic_id: int, subscribe: bool) -> dict | None:
        """Get notified of new posts in a topic.

        API endpoint: PUT topic/subscribe

        Args:
            topic_id (int): Topic id to get notifications for.
            subscribe (bool): True to create activity alert. False to remove it.

        Returns:
            dict | None: dict containing the deserialized json returned by the server. None is returned if an exception
                was raised and then subsequently ignored.
        """
        data = {"topic_id": topic_id, "subscribe": subscribe}

        return await self._client.request(method="PUT", endpoint="topic/subscribe", data=data)
