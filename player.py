import random


class Player(object):
    def __init__(self):
        self.numbers = list(range(1, 46))
        random.shuffle(self.numbers)
        self.numbers = self.numbers[:6]
