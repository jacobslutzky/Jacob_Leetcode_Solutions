class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            target_key = target - nums[i]
            if target_key in d:
                return d[target_key], i
            d[nums[i]] = i