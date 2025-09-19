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
        self.spreadsheet = []
        for _ in range(26):
            self.spreadsheet.append([0 for _ in range(rows)])
        self.columns = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}
        self.rows = rows


    def setCell(self, cell: str, value: int) -> None:
        col = self.columns.get(cell[0], None)
        row = int(cell[1:]) - 1
        if col is not None and 0 <= row < self.rows:
            self.spreadsheet[col][row] = value


    def resetCell(self, cell: str) -> None:
        col = self.columns.get(cell[0], None)
        row = int(cell[1:]) - 1
        if col is not None and 0 <= row < self.rows:
            self.spreadsheet[col][row] = 0

    def getValue(self, formula: str) -> int or None:
        result = 0
        col, row = None, None
        for i in range(len(formula)):
            try:
                if formula[i] in self.columns:
                    col = self.columns[formula[i]]
                elif int(formula[i]) - 1 <= self.rows:
                    row = int(formula[i]) - 1
            except ValueError:
                print("Formula is not correct")
                return None
            if col and row:
                result += self.spreadsheet[col][row]
                col, row = None, None

        return result




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
