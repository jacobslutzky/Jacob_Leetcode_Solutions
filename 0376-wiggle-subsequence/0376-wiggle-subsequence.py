class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1]*2 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i][1] = max(dp[i-1][0]+1,dp[i-1][1])
                dp[i][0] = dp[i-1][0]
            elif nums[i] < nums[i-1]:
                dp[i][0] = max(dp[i-1][1]+1, dp[i-1][0])
                dp[i][1] = dp[i-1][1]
        
        return max(dp[-1])