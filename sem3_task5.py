#Баланс скобок через префиксные суммы. Дана строка из символов '(' и ')'. Разрешено удалить не более k символов.
#Можно ли сделать ее правильной скобочной последовательностью?
def canMakeValidWithDeletions(s, k):
    balance = 0
    extra_closed_balance = 0
    
    for i in range(len(s)):
        if (s[i] == '('):
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                extra_closed_balance += 1
                
    total_needed = balance + extra_closed_balance
    return total_needed <= k


import unittest

class TestCanMakeValidWithDeletions(unittest.TestCase):

    def test1(self):
        self.assertTrue(canMakeValidWithDeletions('', 3))

    def test2(self):
        self.assertTrue(canMakeValidWithDeletions('(())))', 4))

    def test3(self):
        self.assertFalse(canMakeValidWithDeletions('(((((((', 2))

    def test4(self):
        self.assertTrue(canMakeValidWithDeletions(')))))))()', 12))
        
    def test5(self):
        self.assertTrue(canMakeValidWithDeletions('(((())))', 5))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
