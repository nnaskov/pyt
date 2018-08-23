class Analyst:
    def __init__(self, startingCash):
        self.cash = startingCash
        self.shorts = 0
        self.longs = 0

    def buyLong(self, stockPrice, amount):
        if self.cash >= stockPrice * amount:
            self.longs += amount
            self.cash -= stockPrice * amount
            return True
        else:
            return False

    def sellLong(self, stockPrice, amount):
        if self.longs >= amount:
            self.longs -= amount
            self.cash += stockPrice * amount
            return True
        else:
            return False

