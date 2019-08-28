from typing import List

class Round(object):
    @staticmethod
    def convertToInt(text): # parse
        text = text.replace(',', '').replace('원', '').replace('.', '')

        try:
            return int(text)
        except:  # catch
            return 0

    def __init__(self, no, prize1, prize2, prize3, prize4, number1, number2, number3, number4, number5, number6, bonus):
        parsedPrize1 = Round.convertToInt(prize1)
        parsedPrize2 = Round.convertToInt(prize2)
        parsedPrize3 = Round.convertToInt(prize3)
        parsedPrize4 = Round.convertToInt(prize4)

        if no <= 87:
            parsedPrize1 = parsedPrize1 / 2
            parsedPrize2 /= 2
            parsedPrize3 /= 2
            parsedPrize4 /= 2

        self._no = no
        self._prizes = {1:parsedPrize1, 2:parsedPrize2, 3:parsedPrize3, 4:parsedPrize4}

        self._bonus = bonus
        self._numbers: List[int] = [number1, number2, number3, number4, number5, number6]

    def getRank(self, playerNumbers):
        count = 0

        for p in playerNumbers:
            if p in self._numbers:
                count += 1

        if count == 6:
            return 1
        if count == 5:
            if self._bonus in playerNumbers:
                return 2
            else:
                return 3
        if count == 4:
            return 4
        if count == 3:
            return 5

        return 6

    def getPrize(self, rank):
        if rank == 5:
            return 5000
        if rank == 6:
            return 0
        return self._prizes[rank]
