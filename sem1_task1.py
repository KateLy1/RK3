#Требуется подсчитать количество последовательностей длины N состоящей из 0 и 1 в которых нет стоящих подряд двух единиц
#Вариант 1
def b_sequences(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return b_sequences(n - 1) + b_sequences(n - 2)

import unittest

class TestB_sequences(unittest.TestCase):

    def test1(self):
        self.assertEqual(b_sequences(2), 3)

    def test2(self):
        self.assertEqual(b_sequences(4), 8)

    def test3(self):
        self.assertEqual(b_sequences(5), 13)

    def test4(self):
        self.assertEqual(b_sequences(1), 2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Вариант 2
def b_sequences2(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 2
    dp = [1, 2]
    i = 2
    while i != n + 1:
        dp.append(dp[i - 1] + dp[i - 2])
        i += 1
    return dp[n]
        
import unittest

class TestB_sequences2(unittest.TestCase):

    def test1(self):
        self.assertEqual(b_sequences2(2), 3)

    def test2(self):
        self.assertEqual(b_sequences2(4), 8)

    def test3(self):
        self.assertEqual(b_sequences2(5), 13)

    def test4(self):
        self.assertEqual(b_sequences2(1), 2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
