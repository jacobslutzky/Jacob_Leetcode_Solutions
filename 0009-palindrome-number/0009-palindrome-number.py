class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        original = x
        while (x > 0):
            rev*=10
            rev += x%10
            x = x // 10
        return rev == original