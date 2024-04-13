class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = {}

        for num in nums:
            if num-1 in d:
                if num in d:
                    d[num].append(d[num-1][0]+1)
                    d[num].sort()
                else:
                    d[num] = [d[num-1][0]+1]
                d[num-1].pop(0)
                if not d[num-1]:
                    del d[num-1]
            else:
                if num in d:
                    d[num].insert(0,1)
                else:
                    d[num]=[1]
        for num in d:
            for n in d[num]:
                if n < 3:
                    return False
        return True