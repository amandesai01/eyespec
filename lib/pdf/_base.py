from pathlib import Path

import pdfplumber
from pdfplumber.pdf import PDF
from pdfplumber.page import Page


def load(path: Path) -> PDF:
    return pdfplumber.open(path.absolute())


def get_pages(pdf: PDF,
              start_from_page_no: int = 1,
              stop_on_page_no: int = None
              ) -> list[Page]:
    return pdf.pages[start_from_page_no - 1:stop_on_page_no] if stop_on_page_no is not None \
        else pdf.pages[start_from_page_no - 1:]


def get_lines(page: Page) -> list[str]:
    return page.extract_text().splitlines()
