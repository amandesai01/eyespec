from ._regexes import HIERARCHY
from ._base import get_tokens_from_pdf
from ._tokenizer import identify_level


def get_total_index_levels() -> int:
    return len(HIERARCHY)
