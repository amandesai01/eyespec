import json

tokens: list[dict] = None

with open("./tokens.json") as f:
    tokens = json.load(f)

query = {
    "0": {
        "d1": "23",
        "d2": "21",
        "d3": "23",
    }
}

result = None

matches = []
for token in tokens:
    tokenType = str(token["tokenType"])
    tokenMeta = token["tokenMeta"]
    queryForToken = query.get(tokenType)
    if queryForToken:
        is_match = False
        for key, value in tokenMeta.items():
            if key in queryForToken.keys() and value == queryForToken[key]:
                matches.append(token)

print(matches)
