class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                count = 1
                while nums[i]+count in nums_set:
                    count+=1
                max_count = max(count,max_count)
        return max_count

