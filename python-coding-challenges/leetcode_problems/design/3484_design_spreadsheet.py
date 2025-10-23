"""LC 3484. Design Spreadsheet
Link: https://leetcode.com/problems/design-spreadsheet/

API expected:
  - Spreadsheet(rows: int)            -> initialize a spreadsheet with given row count (cols implicit or unlimited)
  - setCell(cell: str, value: int)    -> set a single cell (e.g. "A1") to an integer value
  - resetCell(cell: str)              -> clear/reset a cell to 0 (or default)
  - getValue(formula: str) -> int     -> evaluate a formula string (single ref or sum of refs/ranges)

Notes:
  - Cell identifiers are Excel-like, e.g. "A1", "B2".
  - Formulas may be like "A1", "A1+B2", "SUM(A1:B3)" depending on the task spec.
  - Storage can be sparse (dict), defaulting to 0 for unset cells.
"""

class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.grid = [[0 for _ in range(rows)] for _ in range(self.cols)]
        self.columns = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}

    def _parse_cell(self, cell: str):
        if not cell:
            return None
        col_letter = cell[0].upper()
        if col_letter not in self.columns:
            return None
        col = self.columns[col_letter]
        # parse numeric suffix
        i = 1
        while i < len(cell) and cell[i].isdigit():
            i += 1
        if i == 1:  # no digits
            return None
        row = int(cell[1:i]) - 1
        if 0 <= row < self.rows:
            return (col, row)
        return None

    def setCell(self, cell: str, value: int) -> None:
        pos = self._parse_cell(cell)
        if pos is None:
            return
        c, r = pos
        self.grid[c][r] = value


    def resetCell(self, cell: str) -> None:
        pos = self._parse_cell(cell)
        if pos is None:
            return
        c, r = pos
        self.grid[c][r] = 0

    def getValue(self, formula: str) -> int:
        s = formula.strip()
        if s.startswith('='):
            s = s[1:]
        if not s:
            return 0

        total = 0
        for token in s.split('+'):
            token = token.strip()
            if not token:
                continue
            if token.lstrip('+-').isdigit():
                total += int(token)
                continue
            pos = self._parse_cell(token)
            if pos is not None:
                c, r = pos
                total += self.grid[c][r]
        return total




# ----- Runnable scaffolding examples -----

sheet = Spreadsheet(3)
sheet.setCell("A1", 5)
sheet.setCell("B1", 7)
print(sheet.getValue("A1"))       # expected 5
print(sheet.getValue("B1"))       # expected 7

sheet.resetCell("A1")
print(sheet.getValue("A1"))       # expected 0

# A more complex example (once implemented):
# sheet.setCell("A2", 2)
# sheet.setCell("A3", 3)
# print(sheet.getValue("SUM(A2:A3)"))  # expected 5
