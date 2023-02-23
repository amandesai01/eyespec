from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell.cell import Cell


class XlsxWriter:
    def __init__(self, wb: Workbook):
        self.wb: Workbook = wb
        self.active_ws: Worksheet = wb.active

    def write_2d_array(self, content: list[list[any]], start_from_row=1, start_from_col=1):
        if len(content) == 0:
            return
        end_on_row = start_from_row + len(content) - 1
        total_cells_in_a_row = len(content[0])
        end_on_col = start_from_col + total_cells_in_a_row - 1
        for row_index, row in enumerate(self.active_ws.iter_rows(
            min_row=start_from_row,
            max_row=end_on_row,
            min_col=start_from_col,
            max_col=end_on_col,
        )):
            for cell_index, cell in enumerate(row):
                cell: Cell = cell
                cell.value = str(content[row_index][cell_index])
