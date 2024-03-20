class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        d = {}
        for stone in stones:
            d[stone] = set()
        d[1] = [1]
       
        for i in range(len(stones[1:])):
            for dist in d[stones[i]]:
                for offset in (-1,0,1):
                    if dist + offset > 0 and stones[i] + dist + offset in d:
                        d[stones[i] + dist + offset].add(dist+offset)
        
        return len(d[stones[-1]]) >= 1