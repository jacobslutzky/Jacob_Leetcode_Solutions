class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = [0]*10

        start = 0
        max_size = 0
        for end in range(len(nums)):
            counts[nums[end]]+=1
            while start < end and counts[nums[end]] > k:
                counts[nums[start]] -=1
                start+=1
            max_size = max(max_size, end-start+1)
        return max_size
