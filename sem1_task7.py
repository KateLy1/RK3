#Дана строка s. Необходимо найти максимальную подстроку, которая является палиндромом
#Вариант 1. Два указателя

def longestPalindrome(s):

    def expandAroundCenter(l, r, currentMaxLeft, currentMaxRight):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            if (r - l) > (currentMaxRight - currentMaxLeft):
                currentMaxRight = r
                currentMaxLeft = l
            l -= 1
            r += 1
        return currentMaxLeft, currentMaxRight
    
    currentMaxLeft = 0
    currentMaxRight = 0        
    for i in range(len(s)):
        currentMaxLeft, currentMaxRight = expandAroundCenter(i, i, currentMaxLeft, currentMaxRight)
        currentMaxLeft, currentMaxRight = expandAroundCenter(i, i + 1, currentMaxLeft, currentMaxRight)

    return s[currentMaxLeft : currentMaxRight + 1]

import unittest

class TestLongestPalindrome(unittest.TestCase):

    def test1(self):
        self.assertEqual(longestPalindrome('a'), 'a')

    def test2(self):
        self.assertEqual(longestPalindrome(''), '')

    def test3(self):
        self.assertEqual(longestPalindrome('ab'), 'a')

    def test4(self):
        self.assertEqual(longestPalindrome('ababad'), 'ababa')
        
    def test5(self):
        self.assertEqual(longestPalindrome('rbaabd'), 'baab')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Вариант 2
def longestPalindrome2(s):
    n = len(s)
    dp = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(False)
        dp.append(tmp)
        
    max_length = 1
    start = 0
    
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_length = 2
            start = i
    
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    max_length = length
                    start = i
    
    return s[start:start + max_length]

import unittest

class TestLongestPalindrome2(unittest.TestCase):

    def test1(self):
        self.assertEqual(longestPalindrome2('a'), 'a')

    def test2(self):
        self.assertEqual(longestPalindrome2(''), '')

    def test3(self):
        self.assertEqual(longestPalindrome2('ab'), 'a')

    def test4(self):
        self.assertEqual(longestPalindrome2('ababad'), 'ababa')
        
    def test5(self):
        self.assertEqual(longestPalindrome2('rbaabd'), 'baab')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
