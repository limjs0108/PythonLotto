import openpyxl

wb = openpyxl.load_workbook('excel.xlsx')
ws = wb.active

for r in ws.rows:
    if r[0].row < 4:
        continue

    print(r[1].value, r[4].value, r[6].value, r[8].value, r[10].value, r[13].value, r[14].value, r[15].value, r[16].value, r[17].value, r[18].value, r[19].value)