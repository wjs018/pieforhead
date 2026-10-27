from io import IOBase
from os import PathLike
from pathlib import Path
from typing import BinaryIO

from .clients import AsyncPieFedClient, PieFedClient
from .exceptions import ImageException


class Image:
    """Class to hold image endpoints."""

    def __init__(self, client: PieFedClient):
        self._client = client

    def upload(
        self,
        image: str | BinaryIO | PathLike | tuple[str, bytes | bytearray, str],
        other_endpoint: str | None = None,
    ) -> dict | None:
        """General function for uploading an image.

        Args:
            image (str | BinaryIO | PathLike | tuple[str, bytes  |  bytearray, str]): image to upload. Tuple argument
                must have form suitable for httpx.request, meaning that it is of the form:
                (filename, image_bytes, mime_type).
            other_endpoint (str | None, optional): Used to divert request to one of the other upload endpoints.
                Defaults to None.

        Raises:
            ImageException: raised if image type isn't understood or if unknown endpoint is provided

        Returns:
            dict | None: returns dict if successful and None if there is an error and exceptions were suppressed by the
                client.
        """

        opened_file = False
        file_obj = None

        try:
            # Figure out how to handle the image depending on the type provided
            if isinstance(image, str | PathLike):
                path = Path(image)
                opened_file = True
                file_obj = path.open("rb")
            elif isinstance(image, tuple):
                file_obj = image
            elif isinstance(image, IOBase):
                file_obj = image
                file_obj.seek(0)
            else:
                if self._client.raise_exceptions:
                    raise ImageException(f"Incompatible image type provided for upload: {type(image)}")
                return

            if not other_endpoint:
                endpoint = "upload/image"
            elif other_endpoint == "community":
                endpoint = "upload/community_image"
            elif other_endpoint == "user":
                endpoint = "upload/user_image"
            else:
                if self._client.raise_exceptions:
                    raise ImageException(f"Unknown image endpoint provided: {other_endpoint}")
                return

            files = {"file": file_obj}
            return self._client.request(method="POST", endpoint=endpoint, files=files)
        finally:
            # Make sure to still close the file object no matter what happened with the request
            if opened_file:
                file_obj.close()

    def upload_community_image(
        self,
        image: str | BinaryIO | PathLike | tuple[str, bytes | bytearray, str],
    ) -> dict | None:
        return self.upload(image=image, other_endpoint="community")

    def upload_user_image(
        self,
        image: str | BinaryIO | PathLike | tuple[str, bytes | bytearray, str],
    ) -> dict | None:
        return self.upload(image=image, other_endpoint="user")

    def delete(self, url: str) -> dict | None:
        """Delete an uploaded image by providing its url.

        Args:
            url (str): url of the uploaded image to delete

        Returns:
            dict | None: should be {"result": "ok"} if successful. None if there is an exception that is suppressed
        """
        return self._client.request(method="POST", endpoint="image/delete", data={"file": url})


class ImageAsync:
    """Class to hold async image endpoints."""

    def __init__(self, client: AsyncPieFedClient):
        self._client = client

    async def upload(
        self,
        image: str | BinaryIO | PathLike | tuple[str, bytes | bytearray, str],
        other_endpoint: str | None = None,
    ) -> dict | None:
        """General function for uploading an image.

        Args:
            image (str | BinaryIO | PathLike | tuple[str, bytes  |  bytearray, str]): image to upload. Tuple argument
                must have form suitable for httpx.request, meaning that it is of the form:
                (filename, image_bytes, mime_type).
            other_endpoint (str | None, optional): Used to divert request to one of the other upload endpoints.
                Defaults to None.

        Raises:
            ImageException: raised if image type isn't understood or if unknown endpoint is provided

        Returns:
            dict | None: returns dict if successful and None if there is an error and exceptions were suppressed by the
                client.
        """

        opened_file = False
        file_obj = None

        try:
            # Figure out how to handle the image depending on the type provided
            if isinstance(image, str | PathLike):
                path = Path(image)
                opened_file = True
                file_obj = path.open("rb")
            elif isinstance(image, tuple):
                file_obj = image
            elif isinstance(image, IOBase):
                file_obj = image
                file_obj.seek(0)
            else:
                if self._client.raise_exceptions:
                    raise ImageException(f"Incompatible image type provided for upload: {type(image)}")
                return

            if not other_endpoint:
                endpoint = "upload/image"
            elif other_endpoint == "community":
                endpoint = "upload/community_image"
            elif other_endpoint == "user":
                endpoint = "upload/user_image"
            else:
                if self._client.raise_exceptions:
                    raise ImageException(f"Unknown image endpoint provided: {other_endpoint}")
                return

            files = {"file": file_obj}
            return await self._client.request(method="POST", endpoint=endpoint, files=files)
        finally:
            # Make sure to still close the file object no matter what happened with the request
            if opened_file:
                file_obj.close()

    async def upload_community_image(
        self,
        image: str | BinaryIO | PathLike | tuple[str, bytes | bytearray, str],
    ) -> dict | None:
        return await self.upload(image=image, other_endpoint="community")

    async def upload_user_image(
        self,
        image: str | BinaryIO | PathLike | tuple[str, bytes | bytearray, str],
    ) -> dict | None:
        return await self.upload(image=image, other_endpoint="user")

    async def delete(self, url: str) -> dict | None:
        """Delete an uploaded image by providing its url.

        Args:
            url (str): url of the uploaded image to delete

        Returns:
            dict | None: should be {"result": "ok"} if successful. None if there is an exception that is suppressed
        """
        return await self._client.request(method="POST", endpoint="image/delete", data={"file": url})
