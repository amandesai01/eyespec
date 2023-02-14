import json
import traceback

tokens: list[dict] = []

with open("./tokens.json") as f:
    tokens = json.load(f)


def extract_acceptable_manufacturers(section: dict):
    # SECTION > PART 2 Products > 2.1 Acceptable Manufacturers
    ams = {
        "sectionDetails": {
            "d1": None,
            "d2": None,
            "d3": None,
            "title": None,
        },
        "ams": [
            # {
            #     "title": None,
            #     "content": None,
            #     "backref": None
            # }
        ]
    }
    try:
        sectionDetails = ams["sectionDetails"]
        sectionDetails["title"] = section["tokenMeta"]["title"]
        sectionDetails["d1"] = section["tokenMeta"]["d1"]
        sectionDetails["d2"] = section["tokenMeta"]["d2"]
        sectionDetails["d3"] = section["tokenMeta"]["d3"]
        if len(section.get("data")):
            parts = section["data"]
            for part in parts:
                if part["tokenType"] == 6:
                    if not sectionDetails["title"]:
                        sectionDetails["title"] = part["tokenMeta"]["data"]
                elif part["tokenType"] == 1:
                    if part["tokenMeta"]["name"] == "PRODUCTS":
                        productSections = part["data"]
                        for productSection in productSections:
                            if productSection["tokenMeta"].get("name") == "ACCEPTABLE MANUFACTURERS":
                                manufSections = productSection["data"]
                                amss = ams["ams"]
                                for maufSection in manufSections:
                                    amss.append({
                                        "title": maufSection["tokenMeta"]["data"],
                                        "contents": maufSection["data"],
                                        "backRef": maufSection
                                    })

        return ams
    except:
        traceback.print_exc()

processedSections = []

for token in tokens:
    current_section = None
    token_meta = token["tokenMeta"]
    if token.get("tokenType") == 0:
        processedSections.append(extract_acceptable_manufacturers(token))

print(processedSections)
