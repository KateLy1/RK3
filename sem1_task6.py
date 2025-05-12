#Дан массив целых чисел coin, где каждое число - номинал монеты и некоторое число amount - сумма монет из массива. 
#Необходимо найти наименьшее количество монет, которое в сумме дало бы amount. Если такой комбинации нет - возвращаем -1
#Вариант 1
def coinChange(coins, amount, cache = None):
    if cache is None:
        cache = {}
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in cache:
        return cache[amount]
    minCoins = float('inf')
    for coin in coins:
        res = coinChange(coins, amount - coin, cache)
        if res >= 0 and res < minCoins:
            minCoins = res + 1
    if minCoins == float('inf'):
        cache[amount] = -1
    else:
        cache[amount] = minCoins
    return cache[amount]


import unittest

class TestCoinChange(unittest.TestCase):

    def test1(self):
        self.assertEqual(coinChange([1, 2], 0), 0)

    def test2(self):
        self.assertEqual(coinChange([1,2,5], 11), 3)

    def test3(self):
        self.assertEqual(coinChange([2], 3), -1)

    def test4(self):
        self.assertEqual(coinChange([1,2,5, 17], 3), 2)
        
    def test5(self):
        self.assertEqual(coinChange([8, 9, 12, 16, 18], 16), 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Вариант 2
def coinChange2(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float('inf'):
        return -1;
    return dp[amount]

import unittest

class TestCoinChange2(unittest.TestCase):

    def test1(self):
        self.assertEqual(coinChange2([1, 2], 0), 0)

    def test2(self):
        self.assertEqual(coinChange2([1,2,5], 11), 3)

    def test3(self):
        self.assertEqual(coinChange2([2], 3), -1)

    def test4(self):
        self.assertEqual(coinChange2([1,2,5, 17], 3), 2)
        
    def test5(self):
        self.assertEqual(coinChange2([8, 9, 12, 16, 18], 16), 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
