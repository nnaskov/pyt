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

    def getTotalEquity(self, currentLongPrice, currentShortPrice):
        return self.cash + self.longs.totalEquity(currentLongPrice) + self.shorts.totalEquity(currentShortPrice)

    def getPortfolio(self, currentLongPrice, currentShortPrice):
        total = self.getTotalEquity(currentLongPrice, currentShortPrice)
        return (self.cash/total, self.longs.totalEquity(currentLongPrice) / total, self.shorts.totalEquity(currentShortPrice) / total)

    '''
    desLongs - desired percentage of longs in the portfolio
    desShorts - desired percentage of shorts in the portfolio
    '''
    def rebalancePortfolio(self, desLongs, desShorts, currentLongPrice, currentShortPrice):
        # if cash eqLongs < longPer
        perCash, perLongs, perShorts = self.getPortfolio(currentLongPrice, currentShortPrice)
        total = self.getTotalEquity(currentLongPrice, currentShortPrice)

        def rebalance(des, per, currentPrice, stockHolding):
            #Longs
            perDifference = des - per # How many percent we need to change our longs
            # This is the amount of money we need to change e.g. buy 1000$ or sell 1000$ if negative
            eqChange = total * perDifference
            amountOfShares = int(abs(eqChange) / currentPrice)

            if(eqChange>0):
                self.buy(currentPrice, amountOfShares, stockHolding)
            else:
                self.sell(currentPrice, amountOfShares, stockHolding)

        rebalance(desLongs, perLongs, currentLongPrice, self.longs)
        rebalance(desShorts, perShorts, currentShortPrice, self.shorts)

    # This is the main algorithm
    def act(self, currentLongPrice, currentShortPrice):
        eqCash, eqLongs, eqShorts = self.getPortfolio(currentLongPrice, currentShortPrice)
        if eqCash == 1:
            self.rebalancePortfolio(.45, .30, currentLongPrice, currentShortPrice)
        