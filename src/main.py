from pathlib import Path

from src.lex import get_tokens_from_pdf
from src.pdf import load
from src.parser import create_parse_tree


path_to_pdf = Path('../test-case-1.pdf')

pdf = load(path_to_pdf)
tokens = get_tokens_from_pdf(pdf)

parse_tree = create_parse_tree(tokens)

print(parse_tree)
