from typing import TypedDict


__version__ = "0.0.4"


class ExtraField(TypedDict):
    id: int | None
    label: str | None
    text: str | None
