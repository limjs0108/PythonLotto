# p = Player()
# p.generateNumbers()
# print(p.numbers)

rankCounts = {}
for i in range(1, 7):
    rankCounts[i] = 0

prizeSum = 10000000
cost = 873000

# 회차별 랭크와 당첨금을 구한다.

print(rankCounts)
print(f'획득 금액 : {prizeSum:,}')
print(f'지불 금액 : {cost:,}')
print(f'수익률 : {(prizeSum - cost) / cost:%}')






# wb = openpyxl.load_workbook('excel.xlsx')
# ws = wb.active
#
# for r in ws.rows:
#     if r[0].row < 4:
#         continue
#
#     print(r[1].value, r[4].value, r[6].value, r[8].value, r[10].value, r[13].value, r[14].value, r[15].value, r[16].value, r[17].value, r[18].value, r[19].value)