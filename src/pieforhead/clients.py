import json
import logging

import httpx
import semver

from .exceptions import PieFedClientException
from .utils import VERSION


logger = logging.getLogger(__name__)


class BaseClient:
    """Class that both synchronous and async clients inherit from."""

    instance_url: str
    timeout: float = 5.0
    api_version: str = "alpha"
    headers: dict = {}
    jwt_token: str = ""
    current_username_or_email: str = ""
    current_password: str = ""
    _nodeinfo: dict = {}
    _instance_version: semver.Version = None

    def __init__(
        self,
        instance_url: str,
        timeout: float = 5.0,
        api_version: str = "alpha",
    ):
        """Constructor for base client class.

        Args:
            instance_url str: url of the piefed instance e.g. https://site.tld
            timeout (float, optional): Timeout value for requests. Defaults to 5.0.
            api_version (str, optional): Version of the PieFed API. Defaults to "alpha".
        """
        self.instance_url = instance_url
        self.timeout = timeout
        self.api_version = api_version
        self.headers = {"User-Agent": f"pieforhead/{VERSION}", "Accept": "application/json"}


class PieFedClient(BaseClient):
    """Synchronous client for handling network requests."""

    _client: httpx.Client = None

    def __init__(
        self,
        instance_url: str,
        timeout: float = 5.0,
        api_version: str = "alpha",
        existing_client: httpx.Client = None,
    ):
        """Constructor for Synchronous client.

        Args:
            instance_url str: url of the piefed instance e.g. https://site.tld
            timeout (float, optional): Timeout value for requests. Defaults to 5.0.
            api_version (str, optional): Version of the PieFed API. Defaults to "alpha".
            existing_client (httpx.Client, optional): Pass an httpx.Client object to reuse it (mainly used for tests).
                Defaults to None.
        """
        super().__init__(instance_url=instance_url, timeout=timeout, api_version=api_version)

        base_url = f"{instance_url}/api/{api_version}/"

        if existing_client:
            self._client = existing_client
        else:
            self._client = httpx.Client(headers=self.headers, timeout=self.timeout, base_url=base_url)

    def request(self, method: str, endpoint: str, params: dict = {}, data: dict = {}) -> dict:
        """Function to handle network requests.

        Args:
            method (str): HTTP method for the request, one of ["GET", "POST", "PUT"]
            endpoint (str): API endpoint to send request to e.g. "post/list"
            params (dict, optional): url parameters for the request (only for "GET") Defaults to {}.
            data (dict, optional): json payload for the request ("POST" and "PUT") Defaults to {}.

        Raises:
            PieFedClientException: should also include error message returned from server if available

        Returns:
            dict: deserialized json returned by the server
        """

        if self.jwt_token and "Authorization" not in self.headers:
            self.headers["Authorization"] = "Bearer " + self.jwt_token

        try:
            # Make the request
            logger.debug(f"method={method}, endpoint={endpoint}, params={params}, data={data}")

            resp = self._client.request(
                method=method,
                url=endpoint,
                headers=self.headers,
                timeout=self.timeout,
                params=params,
                json=data,
            )

            resp.raise_for_status()

            # Everything went well
            return resp.json()

        except httpx.HTTPStatusError as e:
            # Server returned a bad status code, try to pull out the returned error message
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} failed with status {resp.status_code}"
            try:
                # A try...except inside a try...except kinda sucks - but more information is better, right?
                error_body = resp.json()
            except json.decoder.JSONDecodeError:
                error_body = {}

            if error_body and error_body.get("message", ""):
                message += f": {error_body['message']}"

            raise PieFedClientException(message) from e

        except httpx.TimeoutException as e:
            # Server timed out
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} timed out"
            raise PieFedClientException(message) from e

        except httpx.RequestError as e:
            # Some other problem with the request
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} failed"
            raise PieFedClientException(message) from e

        except json.decoder.JSONDecodeError as e:
            # Server returned something that isn't JSON
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} did not return parseable JSON"
            raise PieFedClientException(message) from e

    def close(self):
        self._client.close()

    def log_in(self, username_or_email: str, password: str) -> bool:
        payload = {"username": username_or_email, "password": password}
        method = "POST"

        resp = self.request(method=method, endpoint="user/login", data=payload)

        self.jwt_token = resp["jwt"]
        self.headers["Authorization"] = "Bearer " + self.jwt_token
        self.current_username_or_email = username_or_email
        self.current_password = password

        return True

    def is_logged_in(self) -> bool:
        return bool(self.jwt_token)

    def log_out(self) -> bool:
        method = "POST"

        _ = self.request(method=method, endpoint="user/logout")
        self.jwt_token = ""
        self.current_username_or_email = ""
        self.current_password = ""

        return True

    @property
    def nodeinfo(self) -> dict:
        """Dict containing the instance's nodeinfo output.

        Returns:
            dict: deserialized copy of the instance's nodeinfo
        """
        if self._nodeinfo:
            return self._nodeinfo

        method = "GET"
        endpoint = self.instance_url + "/nodeinfo/2.1.json"

        resp = self.request(method=method, endpoint=endpoint)
        self._nodeinfo = resp

        return self._nodeinfo if self._nodeinfo else {}

    @property
    def instance_version(self) -> semver.Version:
        """The instance's software version from the nodeinfo.

        Returns:
            semver.Version: software version of the piefed instance
        """
        version_str = self.nodeinfo["software"]["version"]

        try:
            self._instance_version = semver.Version.parse(version_str)
            return self._instance_version
        except ValueError as e:
            logger.error(msg=str(e))
            logger.error(f"_instance_version={version_str}")

            raise PieFedClientException(f"Instance version from nodeinfo not parseable: {version_str}")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class AsyncPieFedClient(BaseClient):
    """Asynchronous client for handling network requests."""

    _client: httpx.AsyncClient = None

    def __init__(
        self,
        instance_url: str,
        timeout: float = 5.0,
        api_version: str = "alpha",
        existing_client: httpx.AsyncClient = None,
    ):
        """Constructor for Asynchronous client.

        Args:
            instance_url str: url of the piefed instance e.g. https://site.tld
            timeout (float, optional): Timeout value for requests. Defaults to 5.0.
            api_version (str, optional): Version of the PieFed API. Defaults to "alpha".
            existing_client (httpx.Client, optional): Pass an httpx.Client object to reuse it (mainly used for tests).
                Defaults to None.
        """
        super().__init__(instance_url=instance_url, timeout=timeout, api_version=api_version)

        base_url = f"{instance_url}/api/{api_version}/"

        if existing_client:
            self._client = existing_client
        else:
            self._client = httpx.AsyncClient(headers=self.headers, timeout=self.timeout, base_url=base_url)

    async def request(self, method: str, endpoint: str, params: dict = {}, data: dict = {}) -> dict:
        """Async function to handle network requests.

        Args:
            method (str): HTTP method for the request, one of ["GET", "POST", "PUT"]
            endpoint (str): API endpoint to send request to e.g. "post/list"
            params (dict, optional): url parameters for the request (only for "GET") Defaults to {}.
            data (dict, optional): json payload for the request ("POST" and "PUT") Defaults to {}.

        Raises:
            PieFedClientException: should also include error message returned from server if available

        Returns:
            dict: deserialized json returned by the server
        """

        if self.jwt_token and "Authorization" not in self.headers:
            self.headers["Authorization"] = "Bearer " + self.jwt_token

        try:
            # Make the request
            logger.debug(f"method={method}, endpoint={endpoint}, params={params}, data={data}")

            resp = await self._client.request(
                method=method, url=endpoint, headers=self.headers, timeout=self.timeout, params=params, json=data
            )

            resp.raise_for_status()

            # Everything went well
            return resp.json()

        except httpx.HTTPStatusError as e:
            # Server returned a bad status code, try to pull out the returned error message
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} failed with status {resp.status_code}"
            try:
                # A try...except inside a try...except kinda sucks - but more information is better, right?
                error_body = resp.json()
            except json.decoder.JSONDecodeError:
                error_body = {}

            if error_body and error_body.get("message", ""):
                message += f": {error_body['message']}"

            raise PieFedClientException(message) from e

        except httpx.TimeoutException as e:
            # Server timed out
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} timed out"
            raise PieFedClientException(message) from e

        except httpx.RequestError as e:
            # Some other problem with the request
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} failed"
            raise PieFedClientException(message) from e

        except json.decoder.JSONDecodeError as e:
            # Server returned something that isn't JSON
            logger.error(msg=str(e))

            message = f"{method} request to {endpoint} did not return parseable JSON"
            raise PieFedClientException(message) from e

    async def aclose(self):
        await self._client.aclose()

    async def close(self):
        await self.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.aclose()

    async def log_in(self, username_or_email: str, password: str) -> bool:
        payload = {"username": username_or_email, "password": password}
        method = "POST"

        resp = await self.request(method=method, endpoint="user/login", data=payload)

        self.jwt_token = resp["jwt"]
        self.headers["Authorization"] = "Bearer " + self.jwt_token
        self.current_username_or_email = username_or_email
        self.current_password = password

        return True

    async def is_logged_in(self) -> bool:
        return bool(self.jwt_token)

    async def log_out(self) -> bool:
        method = "POST"

        _ = await self.request(method=method, endpoint="user/logout")
        self.jwt_token = ""
        self.current_username_or_email = ""
        self.current_password = ""

        return True

    @property
    async def nodeinfo(self) -> dict:
        """Dict containing the instance's nodeinfo output.

        Returns:
            dict: deserialized copy of the instance's nodeinfo
        """
        if self._nodeinfo:
            return self._nodeinfo

        method = "GET"
        endpoint = self.instance_url + "/nodeinfo/2.1.json"

        resp = await self.request(method=method, endpoint=endpoint)
        self._nodeinfo = resp

        return self._nodeinfo if self._nodeinfo else {}

    @property
    async def instance_version(self) -> semver.Version:
        """The instance's software version from the nodeinfo.

        Returns:
            semver.Version: software version of the piefed instance
        """
        version_str = (await self.nodeinfo)["software"]["version"]

        try:
            self._instance_version = semver.Version.parse(version_str)
            return self._instance_version
        except ValueError as e:
            logger.error(msg=str(e))
            logger.error(f"_instance_version={version_str}")

            raise PieFedClientException(f"Instance version from nodeinfo not parseable: {version_str}")
