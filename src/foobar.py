"""
Test of supporting both v1 and v2 of pydantic

Visit <https://github.com/jwodder/pydantic-v1v2-test> for more information.
"""

from __future__ import annotations
from pathlib import Path
from typing import Literal

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic  # type: ignore[no-redef]


class Foobar(pydantic.BaseModel):
    classname: Literal["Foobar"] = pydantic.Field("Foobar", readOnly=True)
    foo: int
    bar: str

    @classmethod
    def load(cls, file: Path) -> Foobar:
        return cls.parse_raw(file.read_text())


if __name__ == "__main__":
    print(Foobar(foo=42, bar="hello"))
