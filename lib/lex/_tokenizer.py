from re import Match, match as re_match

from lib.tokens import Token, Token0, Token1, Token2,\
                       Token3, Token4, Token5, Token6

from ._regexes import HIERARCHY
from ._utils import clean


def tokenize(raw_strings: list[str], page_no: int = None) -> list[Token]:
    tokens: list[Token] = list()
    for raw_string in raw_strings:
        token: Token = _parse_raw_string(raw_string, page_no)
        if token and _should_accept(token):
            tokens.append(token)
    return tokens


def _parse_raw_string(raw_string: str, page_no: int = None) -> Token:
    for level, pattern in enumerate(HIERARCHY):
        match = re_match(pattern, raw_string)
        if match:
            if level == 0:
                return _tokenize_0(match, page_no)
            elif level == 1:
                return _tokenize_1(match, page_no)
            elif level == 2:
                return _tokenize_2(match, page_no)
            elif level == 3:
                return _tokenize_3(match, page_no)
            elif level == 4:
                return _tokenize_4(match, page_no)
            elif level == 5:
                return _tokenize_5(match, page_no)
            elif level == 6:
                return _tokenize_6(match, page_no)


def identify_level(token: Token) -> int:
    if isinstance(token, Token0):
        return 0
    elif isinstance(token, Token1):
        return 1
    elif isinstance(token, Token2):
        return 2
    elif isinstance(token, Token3):
        return 3
    elif isinstance(token, Token4):
        return 4
    elif isinstance(token, Token5):
        return 5
    elif isinstance(token, Token6):
        return 6
    raise Exception("Unidentified token encountered")


def _should_accept(token: Token) -> bool:
    if isinstance(token, Token6):
        return bool(token.data)
    return True


def _tokenize_0(match: Match, page_no: int) -> Token0:
    raw_digit_string = clean(match.group(1))
    digit_string = raw_digit_string.replace(" ", "")  # Remove spaces
    stubs = digit_string.split(".")
    digits: list[int] = []
    if len(stubs) > 0:
        stub = stubs[0]
        if len(stub) >= 2:
            d1_raw = stub[0:2]
            digits.append(int(d1_raw))
        if len(stub) >= 4:
            d2_raw = stub[2:4]
            digits.append(int(d2_raw))
        if len(stub) > 4:
            d3_raw = stub[4:]
            digits.append(int(d3_raw))
        if len(stubs) > 1:
            stub_2 = stubs[1]
            digits.append(int(stub_2))

    return Token0(
        d1=digits[0] if len(digits) > 0 else None,
        d2=digits[1] if len(digits) > 1 else None,
        d3=digits[2] if len(digits) > 2 else None,
        post_float=digits[3] if len(digits) > 3 else None,
        title=clean(match.group(2)),
        page_no=page_no,
        children=[]
    )


def _tokenize_1(match: Match, page_no: int) -> Token1:
    return Token1(
        sr_no=int(clean(match.group(2))),
        name=clean(match.group(3)),
        page_no=page_no,
        children=[]
    )


def _tokenize_2(match: Match, page_no: int) -> Token2:
    return Token2(
        section=int(clean(match.group(1))),
        sub_section=int(clean(match.group(2))),
        name=clean(match.group(3)),
        page_no=page_no,
        children=[]
    )


def _tokenize_3(match: Match, page_no: int) -> Token3:
    return Token3(
        section=clean(match.group(1)),
        data=clean(match.group(2)),
        page_no=page_no,
        children=[]
    )


def _tokenize_4(match: Match, page_no: int) -> Token4:
    return Token4(
        section=int(clean(match.group(1))),
        data=clean(match.group(2)),
        page_no=page_no,
        children=[]
    )


def _tokenize_5(match: Match, page_no: int) -> Token5:
    return Token5(
        section=clean(match.group(1)),
        data=clean(match.group(2)),
        page_no=page_no,
        children=[]
    )


def _tokenize_6(match: Match, page_no: int) -> Token6:
    return Token6(
        data=clean(match.group(1)),
        page_no=page_no,
        children=[]
    )
