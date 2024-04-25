class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_low = 1
        curr_high = 1
        max_high = -float("inf")
        for i in range(len(nums)):
            curr_low *= nums[i]
            curr_high *= nums[i]

            if curr_low > curr_high:
                curr_low, curr_high = curr_high, curr_low
            max_high = max(max_high, curr_high)
            curr_high = max(1, curr_high)
            curr_low = min(curr_low, 1)

           

        return max_high

