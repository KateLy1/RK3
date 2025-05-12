#Дан массив целых чисел. Каждое число - стоимость акции. 
#Нам нужно купить максимально дешево, а продать максимально дорого. 
#Сделать это надо за O(n)
def maxProfit(prices):
    profit = 0
    min_price = prices[0]
    for currentPriceIndex in range(1, len(prices)):
        profit = max(profit, prices[currentPriceIndex] - min_price)
        min_price = min(prices[currentPriceIndex], min_price)
    return profit

import unittest

class TestMaxProfit(unittest.TestCase):

    def test1(self):
        self.assertEqual(maxProfit([1, 2]), 1)

    def test2(self):
        self.assertEqual(maxProfit([3]), 0)

    def test3(self):
        self.assertEqual(maxProfit([11, 10, 7, 4]), 0)

    def test4(self):
        self.assertEqual(maxProfit([10, 20, 11, 15]), 10)
        
    def test5(self):
        self.assertEqual(maxProfit([8, 9, 3, 7, 4, 16, 12] ), 13)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
