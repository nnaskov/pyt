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

    def totalEquity(self, currentPrice):
        return self.amount * currentPrice

    def totalCost(self):
        return self.amount * self.avgCost


class Analyst:
    def __init__(self, startingCash):
        self.startingCash = startingCash
        self.cash = startingCash
        self.shorts = StockHolding()
        self.longs = StockHolding()

    def buy(self, stockPrice, amount, stock):
        if self.cash >= stockPrice * amount:
            stock.addPurchases(stockPrice, amount)
            self.cash -= stockPrice * amount
            return True
        else:
            return False

    def sell(self, stockPrice, amount, stock):
        if stock.amount >= amount:
            stock.removePurchases(amount)
            self.cash += stockPrice * amount
            return True
        else:
            return False

    def buyLong(self, stockPrice, amount):
      return self.buy(stockPrice, amount, self.longs)

    def sellLong(self, stockPrice, amount):
        return self.sell(stockPrice, amount, self.longs)

    def buyShort(self, stockPrice, amount):
      return self.buy(stockPrice, amount, self.shorts)

    def sellShort(self, stockPrice, amount):
        return self.sell(stockPrice, amount, self.shorts)

    # This is the main algorithm
    def act(self, currentLongPrice, currentShortPrice):
