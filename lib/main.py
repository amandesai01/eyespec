from pathlib import Path

from openpyxl.workbook import Workbook

from lib.jobs.job001 import SaveDivisionWiseTokenInformation
from lib.xlsx import XlsxWriter

path_to_pdf = Path('../test-case-2.pdf')

# pdf = load(path_to_pdf)
# tokens = get_tokens_from_pdf(pdf)
#
# parse_tree = create_parse_tree(tokens)
# division_wise_tokens = exporters.group_by_division(parse_tree)
#
# print(division_wise_tokens)
wb = Workbook()
xlw = XlsxWriter(wb)
job = SaveDivisionWiseTokenInformation(
    pdf_file_location=path_to_pdf,
    xlsx_writer=xlw,
)

job.run()
