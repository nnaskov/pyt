class StockHolding:
    def __init__(self):
        self.amount = 0
        self.avgCost = 0

    def addPurchases(self, price, amount):
        self.avgCost = (self.amount * self.avgCost + amount * price) / (self.amount + amount)
        self.amount += amount

    def removePurchases(self, amount):
        self.amount -= amount

    def totalReturn(self, currentPrice):
        return (currentPrice - self.avgCost) * self.amount

class Analyst:
    def __init__(self, startingCash):
        self.cash = startingCash
        self.shorts = StockHolding()
        self.longs = StockHolding()

    def buyLong(self, stockPrice, amount):
        if self.cash >= stockPrice * amount:
            self.longs.addPurchases(stockPrice, amount)
            self.cash -= stockPrice * amount
            return True
        else:
            return False

    def sellLong(self, stockPrice, amount):
        if self.longs.amount >= amount:
            self.longs.removePurchases(amount)
            self.cash += stockPrice * amount
            return True
        else:
            return False

