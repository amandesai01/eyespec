from pdfplumber.page import Page
from pdfplumber.pdf import PDF

from lib.pdf import get_pages, get_lines
from lib.tokens import Token

from ._tokenizer import tokenize


def get_tokens_from_pdf(pdf: PDF):
    print("Parsing PDF...")
    tokens: list[Token] = []
    pages: list[Page] = get_pages(pdf)
    for sr_no, page in enumerate(pages):
        page_no = sr_no + 1  # page_no = 1-based indexing, sr_no = 0-based indexing
        print("Processing Page No " + str(page_no) + "...")
        lines: list[str] = get_lines(page)
        tokens.extend(tokenize(lines, page_no))
    print("Found " + str(len(tokens)) + " Tokens...")
    return tokens
