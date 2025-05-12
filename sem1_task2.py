#Определите количество последовательностей из нулей и единиц длины, в которых никакие три единицы не стоят рядом.
def count_sequences(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 2
    if (n == 2):
        return 4
    dp = [1, 2, 4]
    i = 3
    while i != n + 1:
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        i += 1
    return dp[n]

import unittest

class TestCount_sequences(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_sequences(2), 4)

    def test2(self):
        self.assertEqual(count_sequences(4), 13)

    def test3(self):
        self.assertEqual(count_sequences(5), 24)

    def test4(self):
        self.assertEqual(count_sequences(1), 2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
