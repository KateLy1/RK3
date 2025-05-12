#Дан массив не отсортированных чисел. Необходимо найти максимально длинную 
#непрерывную возрастающую последовательность и вернуть ее длину
def findLIS(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
    return max(dp)

import unittest

class TestFindLIS(unittest.TestCase):

    def test1(self):
        self.assertEqual(findLIS([]), 0)

    def test2(self):
        self.assertEqual(findLIS([3]), 1)

    def test3(self):
        self.assertEqual(findLIS([3, 2, 8, 9, 5, 10] ), 3)

    def test4(self):
        self.assertEqual(findLIS([8, 8, 8, 8] ), 1)
        
    def test5(self):
        self.assertEqual(findLIS([1, 2, 7, 9, 0, 10] ), 4)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
