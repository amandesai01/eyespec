from typing_extensions import Self
from dataclasses import dataclass


@dataclass
class Token:
    page_no: int
    children: list[Self]

    def get_token_type(self) -> int:
        pass
