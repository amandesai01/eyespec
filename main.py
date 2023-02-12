import re
import json
import pdfplumber
import traceback

index_levels = [
    re.compile(r"SECTION\s(\d+)\s(\d+)\s(\d+)"), # SECTION 01 01 01
    re.compile(r"(PART\s)([\d])\s*[-\s_]*([*a-zA-Z\d]*)"), # group 1 = part number | group 2 = part name
    re.compile(r"^(\d+)\.(\d+)[\s]*([a-zA-Z0-9 ]+)"), # Eg: 1.1 SUMMARY
    re.compile(r"^([A-Z])\. *(.*)"), # Eg. A. <content>
    re.compile(r"^(\d+)\. *(.*)"), # Eg: 1. <content>
    re.compile(r"^([a-z])\. *(.*)"), # Eg: a. <content>
    re.compile(r"^(.+)")
]

final_parse = []

pdf = pdfplumber.open("./test-case-1.pdf")

def clean(s):
    s = s.strip()
    return s

def should_accept_token(token):
    if token["tokenType"] == 6:
        return bool(token["tokenMeta"]["data"])
    return True

def get_index_level_meta_from_match(match, level):
    if level == 0:
        return {
            "#": "SECTION",
            "d1": clean(match.group(1)),
            "d2": clean(match.group(2)),
            "d3": clean(match.group(3)),
        }
    if level == 1:
        return {
            "#": clean(match.group(2)),
            "name": clean(match.group(3))
        }
    elif level == 2:
        return {
            "#": clean(match.group(1)) + " > " + match.group(2),
            "name": clean(match.group(3))
        }
    elif level in (3, 4, 5):
        return {
            "#": clean(match.group(1)),
            "data": clean(match.group(2)),
        }
    elif level == 6:
        return {
            "data": clean(match.group(1)),
        }

def my_print_json(dic, file="log.json"):
    with open('./' + file, "w") as f:
        json.dump(dic, f, indent=4)

def get_tokens(lines: list[str], page_no: int):
    tokens = []
    for line in lines:
        token = None
        for level, index_level in enumerate(index_levels):
            match = re.match(index_level, line)
            if match:
                token = {
                    "tokenType": level,
                    "tokenMeta": get_index_level_meta_from_match(match, level),
                    "pageNo": page_no
                }
                break
        if token and should_accept_token(token):
            tokens.append(token)

    return tokens

tokens = []
try:
    for page_no, page_raw in enumerate(pdf.pages):
        print("Processing Page No >", page_no + 1)
        text = page_raw.extract_text().splitlines()
        # parts_parsed_copy = copy.deepcopy(parts_parsed)
        tokens.extend(get_tokens(text, page_no + 1))
except KeyboardInterrupt:
    print("Force Stopped")
except:
    traceback.print_exc()

def process_l_i(token: dict, level: int, ongoings: list[dict]):
    ongoings[level] = token
    ongoings[level]["data"] = []
    if level > 0 and ongoings[level - 1]:
        ongoings[level - 1]["data"].append(ongoings[level])
        return
    
    for i in range(level - 1, -1, -1):
        if ongoings[i]:
            ongoings[i]["data"].append(token)
            return
    final_parse.append(token)

# print("writing phase 1 output to file...")
# my_print_json(tokens, file="first-out.json")

print("Processing " + str(len(tokens)) + " tokens.")
ongoings = [None for _ in range(len(index_levels))]
for token in tokens:
    tokenType = int(token.get("tokenType"))
    process_l_i(token, tokenType, ongoings)

print("writing tokens to file...")
my_print_json(final_parse, file="tokens.json")

print("post-processing and structuring tokens...")


############################################################################################################
############################################################################################################


def mid_token(token):
    token_meta_data = token["tokenMeta"].get("data")
    new_token = token["tokenMeta"]
    new_token["data"] = [token_meta_data].extend(token["data"]) if token_meta_data else token["data"]
    new_token["l2"] = True
    new_token["tokenType"] = token["tokenType"]
    return new_token


def end_token(token):
    return {
        "l2": True,
        "data": token["tokenMeta"]["data"]
    }


def get_l2_tokens(l1_tokens):
    for i, l1_token in enumerate(l1_tokens):
        if l1_token.get("l2"):
            continue
        tokenType = int(l1_token["tokenType"])
        if tokenType == 6:
            l1_tokens[i] = end_token(l1_token)
        else:
            l1_tokens[i] = mid_token(l1_token)


final_tokens = tokens
queue = [tokens]
while True:
    if queue:
        tokens = queue.pop(0)
        get_l2_tokens(tokens)
        for l2_final_token in tokens:
            if isinstance(l2_final_token.get("data"), list):
                queue.append(l2_final_token["data"])
    else:
        break

print("Writing l2 tokens to file...")
my_print_json(final_tokens, "l2-tokens.json")