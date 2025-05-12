# Индекс поворота массива. 
def pivotIndex(nums):
    totalSum = 0
    leftSum = 0
    
    for i in range(len(nums)):
        totalSum += nums[i]
        
    for i in range(len(nums)):
        if leftSum == totalSum - leftSum - nums[i]:
            return i
        leftSum += nums[i]
        
        
    return -1


import unittest

class TestPivotIndex(unittest.TestCase):

    def test1(self):
        self.assertEqual(pivotIndex([]), -1)

    def test2(self):
        self.assertEqual(pivotIndex([1, 1, 1, 1]), -1)

    def test3(self):
        self.assertEqual(pivotIndex([3, 6, 9, 1, 8, 10]), 3)

    def test4(self):
        self.assertEqual(pivotIndex([12, 9, 1, 2, 9]), 1)
        
    def test5(self):
        self.assertEqual(pivotIndex([2, 8, 5, 2, 1]), -1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
