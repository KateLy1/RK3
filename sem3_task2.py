#Дан массив целых чисел nums и целое число k. Найдите количество непрерывных подмассивов, сумма которых равна k
def subarraySum(nums, k):
    prefixSum = 0
    prefixCount = {0: 1}
    count = 0
    
    for num in nums:
        prefixSum += num
        if prefixSum - k in prefixCount:
            count += prefixCount[prefixSum - k]
        
        prefixCount[prefixSum] = (prefixCount.get(prefixSum, 0)) + 1
        
    return count

import unittest

class TestSubarraySum(unittest.TestCase):

    def test1(self):
        self.assertEqual(subarraySum([], 0), 0)

    def test2(self):
        self.assertEqual(subarraySum([3, 3, 3], 3), 3)

    def test3(self):
        self.assertEqual(subarraySum([3, 2, 8, 9, 5, 10], 5), 2)

    def test4(self):
        self.assertEqual(subarraySum([8, 10, 4, 18, 4, 3, 19], 22), 4)
        
    def test5(self):
        self.assertEqual(subarraySum([0, 0, 0, 0, 0, 0, 0], 0), 28)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
