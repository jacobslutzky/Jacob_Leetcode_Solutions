class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res += n % 2
            n>>=1
        return res