"""
Test of supporting both v1 and v2 of pydantic

Visit <https://github.com/jwodder/pydantic-v1v2-test> for more information.
"""

from __future__ import annotations
from pathlib import Path

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "foobar@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/pydantic-v1v2-test"

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
