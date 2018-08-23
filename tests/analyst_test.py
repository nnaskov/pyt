import unittest
from analyst import Analyst


class AnalystTestCase(unittest.TestCase):
    def assertAnalyst(self, analyst, expectedCash, expectedLongs, exepctedShorts):
        self.assertEqual(analyst.cash, expectedCash)
        self.assertEqual(analyst.longs, expectedLongs)
        self.assertEqual(analyst.shorts,exepctedShorts)

    def test_init(self):
        a = Analyst(10000)
        self.assertAnalyst(a, 10000, 0, 0)

    def test_buy_long_good(self):
        a = Analyst(10000)
        a.buyLong(50, 3)
        cash = 10000 - 3*50
        self.assertAnalyst(a, cash, 3, 0)

        a.buyLong(55, 10)
        cash -= 55*10
        self.assertAnalyst(a, cash, 13, 0)

    def test_buy_sell_long(self):
        a = Analyst(150)
        a.buyLong(50, 3)
        a.sellLong(55, 3)
        cash = 150 - (3 * 50) + (3 * 55)
        self.assertAnalyst(a, cash, 0, 0)

    def test_buy_sell_bad(self):
        a = Analyst(100)
        buy = a.buyLong(50, 3)
        self.assertFalse(buy)
        self.assertAnalyst(a, 100, 0, 0)

        sell = a.sellLong(55, 3)
        self.assertFalse(sell)
        self.assertAnalyst(a, 100, 0, 0)

if __name__ == '__main__':
    unittest.main()