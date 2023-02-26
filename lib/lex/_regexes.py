from re import compile, Pattern


_TOKEN_0 = compile(r"^ *SECTION\s*([\d \.]*)(.*)") # SECTION 01 01 01
_TOKEN_1 = compile(r"(PART\s)([\d])\s*[-\s_]*([*a-zA-Z\d]*)") # group 1 = part number | group 2 = part name
_TOKEN_2 = compile(r"^ *(\d+)\.(\d+)[\s]*([a-zA-Z0-9 ]+)") # Eg: 1.1 SUMMARY
_TOKEN_3 = compile(r"^ *([A-Z])\. *(.*)") # Eg. A. <content>
_TOKEN_4 = compile(r"^ *(\d+)\. *(.*)") # Eg: 1. <content>
_TOKEN_5 = compile(r"^ *([a-z])\. *(.*)") # Eg: a. <content>
_TOKEN_6 = compile(r"^ *(.+)")

HIERARCHY: list[Pattern] = [
    _TOKEN_0,
    _TOKEN_1,
    _TOKEN_2,
    _TOKEN_3,
    _TOKEN_4,
    _TOKEN_5,
    _TOKEN_6,
]
