from ._base import ParserJob
from lib.parser import exporters


class SaveDivisionWiseTokenInformation(ParserJob):
    def __init__(self, *args, **kwargs):
        super(SaveDivisionWiseTokenInformation, self).__init__(*args, **kwargs)

    def run(self) -> None:
        parse_tree = self.get_parse_tree()
        division_wise_tokens = exporters.group_by_division(parse_tree)
        content: list[list[str]] = []
        for division in division_wise_tokens:
            division_heading_stub = ["Division", division.sr_no]
            content.append(division_heading_stub)
            for section in division.children:
                stub = [section.get_section_hash(), section.title]
                content.append(stub)
            content.append(["", ""])

        self.save_to_xlsx(content)
