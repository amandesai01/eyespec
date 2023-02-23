from pathlib import Path

from pdfplumber.pdf import PDF

from lib.tokens import Token
from lib.parser import create_parse_tree
from lib.lex import get_tokens_from_pdf
from lib.pdf import load as load_pdf_from_path
from lib.xlsx import XlsxWriter


class ParserJob(object):
    def __init__(self,
                 pdf: PDF = None,
                 parse_tree: list[Token] = None,
                 xlsx_writer: XlsxWriter = None,
                 parse_tree_file_location: Path = None,
                 pdf_file_location: Path = None):
        if pdf is None:
            if pdf_file_location:
                self._pdf: PDF = load_pdf_from_path(pdf_file_location)
            else:
                print("No PDF Passed. Automatically calculating parse tree disabled till externally passed...")
        else:
            self._pdf: PDF = pdf

        if parse_tree is None:
            self._parse_tree = None
            if parse_tree_file_location:
                pass  # load from file
            else:
                print("No Parse Tree Passed. Expected to load later...")
        else:
            self._parse_tree: list[Token] = parse_tree

        if xlsx_writer is None:
            print("XLSX Writer None")
        else:
            self._xlsx_writer = xlsx_writer

    def set_parse_tree(self, parse_tree: list[Token]) -> None:
        print("Externally loaded parse tree...")
        self._parse_tree = parse_tree

    def get_parse_tree(self):
        if self._parse_tree is None:
            print("Parse tree is not present. Calculating...")
            self._calculate_parse_tree()
        return self._parse_tree

    def set_pdf(self, pdf: PDF) -> None:
        print("Externally loaded pdf. Parse tree can be now calculated...")
        self._pdf = pdf

    def save_to_xlsx(self, content: list[list[str]]):
        self._xlsx_writer.write_2d_array(content)
        self._xlsx_writer.wb.save("OUTPUT.xlsx")

    def _calculate_parse_tree(self) -> None:
        assert self._pdf is not None
        if self._parse_tree is not None:
            print("Parse tree already present. Recalculating...")
        _raw_tokens = get_tokens_from_pdf(self._pdf)
        self._parse_tree = create_parse_tree(_raw_tokens)

    def run(self) -> None:
        raise NotImplementedError()
