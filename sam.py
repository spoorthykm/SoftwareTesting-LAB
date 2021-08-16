from openpyxl import Workbook
from openpyxl import load_workbook

Workbook = load_workbook(filename='spoo.xlsx')
spreadsheet = Workbook.active

spreadsheet["A1"] = "Hello"
spreadsheet["B1"] = "World!"
Workbook.write('A2', 'Hello')
Workbook.save(filename="spoo.xlsx")
Workbook.close()