from openpyxl import Workbook

workbook = Workbook()
spreadsheet = workbook.active

spreadsheet["A1"] = "spoorthy"
spreadsheet["A2"] = "samhitha"
spreadsheet["A3"] = "sahana"
spreadsheet["A4"] = "Thanmyee"
spreadsheet["B1"] = "100"
spreadsheet["B2"] = "70"
spreadsheet["B3"] = "50"
spreadsheet["B4"] = "45"

workbook.save(filename="students.xlsx")