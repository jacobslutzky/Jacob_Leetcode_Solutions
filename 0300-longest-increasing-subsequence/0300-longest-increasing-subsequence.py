class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [float("inf")]*len(nums)
        longest_subsequence = 0
        for i in range(len(nums)):
            low = 0
            high = longest_subsequence
           
            while low < high:
                mid = low + (high-low)//2
                if nums[i] <= dp[mid]:
                    high = mid
                else:
                    low = mid+1
            dp[low] = nums[i]
            if low == longest_subsequence:
                longest_subsequence+=1
        return longest_subsequence
            


