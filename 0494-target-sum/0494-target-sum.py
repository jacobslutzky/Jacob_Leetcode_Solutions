class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        new_d = {}
        old_d = {nums[0]*1: 1, nums[0]*-1:1}
        
        for num in nums[1:]:
            for n in old_d:
                for i in (-1,1):
                    new_num = num + n*i
                    if new_num in new_d:
                        new_d[new_num] += 1
                    else:
                        new_d[new_num] = old_d[n]
            old_d = new_d
            new_d = {}
        if target in old_d:
            return old_d[target]
        return 0