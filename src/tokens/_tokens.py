from dataclasses import dataclass

from ._base import Token


@dataclass
class Token0(Token):
    d1: int = None
    d2: int = None
    d3: int = None
    title: str = None


@dataclass
class Token1(Token):
    sr_no: int = None
    name: str = None


@dataclass
class Token2(Token):
    section: int = None
    sub_section: int = None
    name: str = None


@dataclass
class Token3(Token):
    section: str = None
    data: str = None


@dataclass
class Token4(Token):
    section: int = None
    data: str = None


@dataclass
class Token5(Token):
    section: str = None
    data: str = None


@dataclass
class Token6(Token):
    data: str = None
