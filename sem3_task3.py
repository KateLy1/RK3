#Максимальная длина подмассива с равным количеством нулей и единиц. Дан бинарный массив
#nums. Найдите максимальную длину подмассива с одинаковым количеством 0 и 1.
def findMaxLength(nums):
    prefixSum = 0
    maxLen = 0
    indexMap = {0: -1}
    
    for i in range(len(nums)):
        num = nums[i]
        if num == 0:
            prefixSum += -1
        else:
            prefixSum += 1
            
        if prefixSum in indexMap:
            maxLen = max(maxLen, i - indexMap[prefixSum])
        else:
            indexMap[prefixSum] = i
            
    return maxLen


import unittest

class TestFindMaxLength(unittest.TestCase):

    def test1(self):
        self.assertEqual(findMaxLength([]), 0)

    def test2(self):
        self.assertEqual(findMaxLength([1, 1, 1, 1]), 0)

    def test3(self):
        self.assertEqual(findMaxLength([1, 1, 1, 0, 0, 0]), 6)

    def test4(self):
        self.assertEqual(findMaxLength([0, 1, 0, 1, 1, 1, 1, 0]), 4)
        
    def test5(self):
        self.assertEqual(findMaxLength([1, 0, 1, 1]), 2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
