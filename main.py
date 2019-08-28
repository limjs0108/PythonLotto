from typing import List
import openpyxl
from player import Player
from round import Round

def loadRounds(filePath: str) -> List[Round]:
    workBook = openpyxl.load_workbook(filePath)
    workSheet = workBook.active

    rounds = []
    for r in workSheet.rows:
        if r[0].row < 4:
            continue

        round = Round(r[1].value, r[4].value, r[6].value, r[8].value, r[10].value, r[13].value, r[14].value, r[15].value,
              r[16].value, r[17].value, r[18].value, r[19].value)
        rounds.append(round)

    return rounds

p = Player()
print(p.numbers)

rankCounts = {}
for i in range(1, 7):
    rankCounts[i] = 0

prizeSum = 0
cost = 0

# 회차별 랭크와 당첨금을 구한다.
rounds: List[Round] = loadRounds('excel.xlsx')
for round in rounds:
    rank: int = round.getRank(p.numbers)
    prize: int = round.getPrize(rank)

    rankCounts[rank] += 1
    prizeSum += prize
    cost += 1000

print(rankCounts)
print(f'획득 금액 : {prizeSum:,}')
print(f'지불 금액 : {cost:,}')
print(f'수익률 : {(prizeSum - cost) / cost:%}')
