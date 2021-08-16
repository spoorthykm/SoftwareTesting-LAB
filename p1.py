import xlsxwriter

workbook = xlsxwriter.Workbook('Example3.xlsx')
worksheet = workbook.add_worksheet("My sheet")
for row in range(1,3):
    print("Enter Name, USN, marks in 3 subjects of student "+str(row))
    for col in range(5):
        ele=input()
        worksheet.write(row,col,ele)