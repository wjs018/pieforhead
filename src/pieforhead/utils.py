from typing import TypedDict


__version__ = "0.1.4"


class ExtraField(TypedDict):
    """Class used for type hinting extra fields."""

    id: int | None
    label: str | None
    text: str | None
