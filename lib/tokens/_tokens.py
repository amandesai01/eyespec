from dataclasses import dataclass, field

from ._base import Token


@dataclass
class Token0(Token):
    d1: int = None
    d2: int = None
    d3: int = None
    post_float: int = None
    title: str = None

    def get_section_hash(self) -> str:
        hash_part_1 = "".join([str(self.d1),
                               str(self.d2),
                               str(self.d3)])
        if not self.post_float:
            return hash_part_1
        hash_part_2 = "." + str(self.post_float)
        return hash_part_1 + hash_part_2

    def get_token_type(self) -> int:
        return 0


@dataclass
class Token1(Token):
    sr_no: int = None
    name: str = None

    def get_token_type(self) -> int:
        return 1

@dataclass
class Token2(Token):
    section: int = None
    sub_section: int = None
    name: str = None

    def get_token_type(self) -> int:
        return 2


@dataclass
class Token3(Token):
    section: str = None
    data: str = None

    def get_token_type(self) -> int:
        return 3


@dataclass
class Token4(Token):
    section: int = None
    data: str = None

    def get_token_type(self) -> int:
        return 4


@dataclass
class Token5(Token):
    section: str = None
    data: str = None

    def get_token_type(self) -> int:
        return 5

@dataclass
class Token6(Token):
    data: str = None

    def get_token_type(self) -> int:
        return 6


@dataclass
class SpecialTokenDivision:
    sr_no: int

    children: list[Token0] = field(default_factory=list)
