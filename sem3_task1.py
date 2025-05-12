#Дан массив целых чисел arr и число k.Требуется найти максимальную сумму среди всех возможных подмассивов длины k
def maxSubarraySum(arr, k):
    if len(arr) < k:
        return None
    
    currentSum = 0
    for i in range(k):
        currentSum += arr[i]
    maxSum = currentSum
    for i in range(k, len(arr)):
        currentSum = currentSum - arr[i - k] + arr[i]
        maxSum = max(maxSum, currentSum)
        
    return maxSum

import unittest

class TestMaxSubarraySum(unittest.TestCase):

    def test1(self):
        self.assertEqual(maxSubarraySum([], 0), 0)

    def test2(self):
        self.assertEqual(maxSubarraySum([3, 2], 10), None)

    def test3(self):
        self.assertEqual(maxSubarraySum([3, 2, 8, 9, 5, 10], 2), 17)

    def test4(self):
        self.assertEqual(maxSubarraySum([8, 10, 4, 18, 8, 3], 3), 32)
        
    def test5(self):
        self.assertEqual(maxSubarraySum([0, 0, 0, 0, 0, 0, 0], 6), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
