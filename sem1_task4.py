#Дано некоторое число n. Необходимо создать треугольник Паскаля состоящего из n строк
#Вариант 1
def pascal_triangle(row, col):
    if col == 0 or row == col:
        return 1
    else:
        return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)

def print_pascal(n):
    dp = []
    for row in range(n):
        currentRow = []
        for col in range(row + 1):
            currentRow.append(pascal_triangle(row, col))
        dp.append(currentRow)
    return dp
        
import unittest

class TestPrint_pascal(unittest.TestCase):

    def test1(self):
        self.assertEqual(print_pascal(0), [])

    def test2(self):
        self.assertEqual(print_pascal(1), [[1]])

    def test3(self):
        self.assertEqual(print_pascal(2), [[1], [1, 1]])

    def test4(self):
        self.assertEqual(print_pascal(6), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
        
    def test5(self):
        self.assertEqual(print_pascal(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#Вариант 2
def pascal_triangle2(n):
    dp = []
    for i in range(1, n + 1):
        tmp = []
        for j in range(1, i + 1):
            tmp.append(1)
        dp.append(tmp)

    for row in range (1, n):
        for col in range(1, row):
            dp[row][col] = dp[row-1][col-1] + dp[row-1][col]
    return dp

import unittest

class TestPascal_triangle2(unittest.TestCase):

    def test1(self):
        self.assertEqual(pascal_triangle2(0), [])

    def test2(self):
        self.assertEqual(pascal_triangle2(1), [[1]])

    def test3(self):
        self.assertEqual(pascal_triangle2(2), [[1], [1, 1]])

    def test4(self):
        self.assertEqual(pascal_triangle2(6), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
        
    def test5(self):
        self.assertEqual(pascal_triangle2(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
