class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones = sorted([a,b,c])
        count = 0
        while stones[1] > 0 and stones[2] > 0:
            if stones[0] > 0:
                stones[0]-=1
            else:
                stones[1]-=1
            stones[2]-=1
            stones.sort()
            count+=1
        return count
        
