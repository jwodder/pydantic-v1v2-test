from __future__ import annotations
from pathlib import Path

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

class Foobar(pydantic.BaseModel):
    foo: int
    bar: str

    @classmethod
    def load(cls, file: Path) -> Foobar:
        return cls.parse_raw(file.read_text())
