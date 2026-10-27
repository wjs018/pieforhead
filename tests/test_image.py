from io import BytesIO
from pathlib import Path
from unittest.mock import Mock

import pytest

from pieforhead.exceptions import ImageException
from pieforhead.image import Image


def make_image(response: dict | None, raise_exceptions: bool = True) -> tuple[Image, Mock]:
    """Make a mock Image class to return toy data.

    Args:
        response (dict | None): value returned from Image._client.request()
        raise_exceptions (bool): whether the client should raise exceptions or not. Defaults to True.

    Returns:
        tuple[Image, Mock]: The Image and the client that were created
    """
    client = Mock()
    client.request.return_value = response
    client.raise_exceptions = raise_exceptions

    return Image(client), client


# tmp_path is a pytest feature that creates a temporary directory for the test (pathlib.Path)
def test_upload_path(tmp_path: Path):
    """Test uploading image by local filename/filepath."""

    # Create the file and write data
    image_path = tmp_path / "image.png"
    image_path.write_bytes(b"image data")

    # Create mock things
    image, client = make_image({"url": "https://site.tld/image.png"})

    # Check the response
    assert image.upload(image=image_path) == {"url": "https://site.tld/image.png"}

    # Check the kwargs
    assert client.request.call_args.kwargs["method"] == "POST"
    assert client.request.call_args.kwargs["endpoint"] == "upload/image"

    # Check some additional info about the file in the request
    file_info = client.request.call_args.kwargs["files"]["file"]
    assert file_info.name == str(image_path)  # Check the filepath
    assert file_info.closed  # Ensure the file is closed


def test_upload_file_object():
    """Test uploading a BytesIO object and ensuring it seeks correctly."""

    # Create the image data and intentionally seek away from the start
    file_obj = BytesIO(b"image data")
    file_obj.seek(4)

    # Create mock things
    image, client = make_image({"url": "https://site.tld/image.png"})

    # Check the response
    assert image.upload(image=file_obj) == {"url": "https://site.tld/image.png"}

    # Check the args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="upload/image",
        files={"file": file_obj},
    )
    assert file_obj.tell() == 0  # Ensure that file was properly seeked to beginning
    assert not file_obj.closed  # Ensure that provided file was not closed


def test_upload_in_context_handler(tmp_path: Path):
    """Test uploading when opening a file in a with block."""

    # Create the file and write data
    image_path = tmp_path / "image.png"
    image_path.write_bytes(b"image data")

    # Create mock things
    image, client = make_image({"url": "https://site.tld/image.png"})

    # with context manager
    with open(image_path, "rb") as im_file:
        # Check the response
        assert image.upload(image=im_file) == {"url": "https://site.tld/image.png"}

    # Check the kwargs
    assert client.request.call_args.kwargs["method"] == "POST"
    assert client.request.call_args.kwargs["endpoint"] == "upload/image"

    # Check some additional info about the file in the request
    file_info = client.request.call_args.kwargs["files"]["file"]
    assert file_info.name == str(image_path)  # Check the filepath
    assert file_info.closed  # Ensure the file is closed


def test_upload_tuple():
    """Uploading an image when a full tuple is provided with bytes data."""

    # Create the tuple and mock things
    image_data = ("image.png", b"image data", "image/png")
    image, client = make_image({"url": "https://site.tld/image.png"})

    # Check the response
    assert image.upload(image=image_data) == {"url": "https://site.tld/image.png"}

    # Check the args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="upload/image",
        files={"file": image_data},
    )


def test_community_endpoint():
    """Ensure proper endpoint is used."""

    # Create data and mock things
    image_data = ("image.png", b"image data", "image/png")
    image, client = make_image({"url": "https://site.tld/image.png"})

    # Check the response
    assert image.upload_community_image(image=image_data) == {"url": "https://site.tld/image.png"}

    # Check the args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="upload/community_image",
        files={"file": image_data},
    )


def test_user_endpoint():
    """Ensure proper endpoint is used."""

    # Create data and mock things
    image_data = ("image.png", b"image data", "image/png")
    image, client = make_image({"url": "https://site.tld/image.png"})

    # Check the response
    assert image.upload_user_image(image=image_data) == {"url": "https://site.tld/image.png"}

    # Check the args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="upload/user_image",
        files={"file": image_data},
    )


def test_invalid_image_type():
    """Make sure improper arg for image is caught before request."""

    # Make mock things
    image, client = make_image({"url": "https://site.tld/image.png"})

    with pytest.raises(ImageException, match="Incompatible image type provided"):
        # An int should throw an exception
        image.upload(image=42)

    # Make sure we stopped execution before making a network request
    client.request.assert_not_called()


def test_invalid_image_type_raising():
    """If the client is set to ignore exceptions, don't raise them."""

    # Make mock things, setting it to ignore exceptions
    image, client = make_image(None, raise_exceptions=False)

    # Ensure attribute is saved to client
    assert client.raise_exceptions is False

    # Invalid args should just return None when ignoring exceptions
    assert image.upload(image=42) is None

    # Make sure network request is not made
    client.request.assert_not_called()


def test_unknown_endpoint(tmp_path: Path):
    # Create data and mock things
    image_data = ("image.png", b"image data", "image/png")
    image, client = make_image({"url": "https://site.tld/image.png"})

    with pytest.raises(ImageException, match="Unknown image endpoint"):
        # Make sure the correct exception is called
        image.upload(image=image_data, other_endpoint="unknown")

    # Make sure that network request is not made
    client.request.assert_not_called()


def test_unknown_endpoint_raising():
    # Create data and mock things
    image_data = ("image.png", b"image data", "image/png")
    image, client = make_image(None, raise_exceptions=False)

    # Ensure attribute is saved to client
    assert client.raise_exceptions is False

    # Should just return None when exception is not raised
    assert image.upload(image=image_data, other_endpoint="unknown") is None

    # Make sure that network request is not made
    client.request.assert_not_called()


def test_delete_image():
    # Make mock things
    response = {"result": "ok"}
    image, client = make_image(response)

    # Check response
    assert image.delete(url="https://site.tld/image.png") == response

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="image/delete",
        data={"file": "https://site.tld/image.png"},
    )


def test_delete_image_raising():
    # Make mock things, simulating None coming from the client request
    image, client = make_image(None, raise_exceptions=False)

    # Ensure attribute is saved to client
    assert client.raise_exceptions is False

    # Should return None when exceptions are suppressed
    assert image.delete(url="https://site.tld/image.png") is None

    # Check args
    client.request.assert_called_once_with(
        method="POST",
        endpoint="image/delete",
        data={"file": "https://site.tld/image.png"},
    )
