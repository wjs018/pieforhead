from typing import TypedDict


__version__ = "0.2.0"


class ExtraField(TypedDict):
    """Class used for type hinting extra fields."""

    id: int | None
    label: str | None
    text: str | None
