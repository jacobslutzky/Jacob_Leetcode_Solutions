class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        d = {1: 0,
            0: 0}
        start = 0
        end = 0
        max_ones = 0
        while end < len(nums):
            if nums[end] == 0:
                d[0]+=1
            else:
                d[1]+=1
            while d[0] > k:
                d[nums[start]]-=1
                start+=1
            max_ones = max(max_ones, d[1]+d[0])
            end+=1
        return max_ones
            