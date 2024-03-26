class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = max(0,max(nums))
        for x in range(len(nums)):
            if nums[x] <= 0:
                nums[x] = 0
        for x in nums:
            x = abs(x)
            if x <= len(nums) and x-1 >=0 and nums[x-1] > 0:
                nums[x-1] *= -1
        print(nums)
        for x in range(len(nums)):
            if nums[x] >= 0:
                return x+1
        return max_num+1