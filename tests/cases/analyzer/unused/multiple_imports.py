from typing import List, Union

from unimport.statement import Import, ImportFrom, Name

NAMES: List[Name] = [
    Name(lineno=12, name="some", is_all=False),
    Name(lineno=13, name="calls", is_all=False),
    Name(lineno=16, name="after", is_all=False),
]
IMPORTS: List[Union[Import, ImportFrom]] = [
    Import(lineno=1, column=1, name="x", package="x"),
    Import(lineno=2, column=1, name="x.y", package="x.y"),
    Import(lineno=3, column=1, name="x.y.z", package="x.y.z"),
    Import(lineno=4, column=1, name="x", package="x"),
    Import(lineno=4, column=2, name="x.y", package="x.y"),
    Import(lineno=5, column=1, name="x", package="x"),
    Import(lineno=5, column=2, name="x.y", package="x.y"),
    Import(lineno=5, column=3, name="x.y.z", package="x.y.z"),
    Import(lineno=6, column=1, name="x.y", package="x.y"),
    Import(lineno=6, column=2, name="x.y.z", package="x.y.z"),
    Import(lineno=6, column=3, name="x.y.z", package="x.y.z"),
    Import(lineno=7, column=1, name="x.y", package="x.y"),
    Import(lineno=7, column=2, name="x.y", package="x.y"),
    Import(lineno=7, column=3, name="x.y.z", package="x.y.z"),
    ImportFrom(
        lineno=8, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=9, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=9, column=2, name="z", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=10,
        column=1,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=10,
        column=2,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=11,
        column=1,
        name="z",
        package="x.y.z",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=11,
        column=2,
        name="q",
        package="x.y.z",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=11,
        column=3,
        name="zq",
        package="x.y.z",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=17, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=20, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=20, column=2, name="z", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=24, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=24, column=2, name="z", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=28,
        column=1,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=28,
        column=2,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=28,
        column=3,
        name="u",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=1,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=2,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=3,
        name="u",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=4,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=5,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
]
UNUSED_IMPORTS: List[Union[Import, ImportFrom]] = [
    ImportFrom(
        lineno=33,
        column=5,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=4,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=3,
        name="u",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=2,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=33,
        column=1,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=28,
        column=3,
        name="u",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=28,
        column=2,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=28,
        column=1,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=24, column=2, name="z", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=24, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=20, column=2, name="z", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=20, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=17, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=11,
        column=3,
        name="zq",
        package="x.y.z",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=11,
        column=2,
        name="q",
        package="x.y.z",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=11,
        column=1,
        name="z",
        package="x.y.z",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=10,
        column=2,
        name="q",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=10,
        column=1,
        name="z",
        package="x.y",
        star=False,
        suggestions=[],
    ),
    ImportFrom(
        lineno=9, column=2, name="z", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=9, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    ImportFrom(
        lineno=8, column=1, name="y", package="x", star=False, suggestions=[]
    ),
    Import(lineno=7, column=3, name="x.y.z", package="x.y.z"),
    Import(lineno=7, column=2, name="x.y", package="x.y"),
    Import(lineno=7, column=1, name="x.y", package="x.y"),
    Import(lineno=6, column=3, name="x.y.z", package="x.y.z"),
    Import(lineno=6, column=2, name="x.y.z", package="x.y.z"),
    Import(lineno=6, column=1, name="x.y", package="x.y"),
    Import(lineno=5, column=3, name="x.y.z", package="x.y.z"),
    Import(lineno=5, column=2, name="x.y", package="x.y"),
    Import(lineno=5, column=1, name="x", package="x"),
    Import(lineno=4, column=2, name="x.y", package="x.y"),
    Import(lineno=4, column=1, name="x", package="x"),
    Import(lineno=3, column=1, name="x.y.z", package="x.y.z"),
    Import(lineno=2, column=1, name="x.y", package="x.y"),
    Import(lineno=1, column=1, name="x", package="x"),
]
