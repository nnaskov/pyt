import numpy as np
import matplotlib.pyplot as plt
from analyst import *
def getRandomPriceMovement():

    trading_seconds_per_day = 8 * 60 * 60

    # the interval in seconds, between each price check
    price_checks_interval = 260

    total_checks = int(trading_seconds_per_day / price_checks_interval)
    # The interval that each movement can go e.g. -0.05% to +0.05%
    movement_interval = 0.005
    startingPrice = 60.0
    movement = np.random.rand(total_checks) * np.array(movement_interval*2)-np.array(movement_interval)

    currentPrice = startingPrice
    arr = []
    for x in np.nditer(movement):
        currentPrice = round(currentPrice + currentPrice * x, 2)
        arr.append(currentPrice)

    return np.array(arr)



# plt.plot(getRandomPriceMovement())
# plt.ylabel('some numbers')
# plt.show()