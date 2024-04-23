class Solution:
    def reverse(self, x: int) -> int:
        new_x = 0
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        while x > 0:
            new_x =(new_x*10) + (x%10)
            x = x // 10
            if new_x*sign < (-2**31) or new_x*sign > (2**31-1):
                return 0
        return new_x * sign
        