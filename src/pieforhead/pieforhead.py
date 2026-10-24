from .clients import PieFedClient


class PieFed:
    _client: PieFedClient
    instance_url: str

    def __init__(self, instance_url: str, timeout: float = 5.0):
        self.instance_url = instance_url.removesuffix("/")
        self._client = PieFedClient(instance_url=instance_url, timeout=timeout)

    def __enter__(self):
        return self

    def log_in(self, username_or_email: str, password: str) -> bool:
        return self._client.log_in(username_or_email, password)

    def is_logged_in(self) -> bool:
        return self._client.is_logged_in()

    def log_out(self) -> bool:
        return self._client.log_out()

    def close(self):
        self._client.close()

    def __exit__(self, *args):
        self.close()

    @property
    def instance_version(self):
        return self._client.instance_version


class PieFedAsync:
    pass
