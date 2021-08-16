import os
from openpyxl import load_workbook,Workbook
wb=Workbook()
ws=wb.active
n=int(input())
ws.append(["name","USN","M!","m2","m3"])
for i in range(n):
	print("entwe",i)
	data=input().split(" ")
	ws.append([data[0],data[1],data[2],data[3],data[4]])
wb.save("stt.xlsx")
os.system("stt.xlxs")