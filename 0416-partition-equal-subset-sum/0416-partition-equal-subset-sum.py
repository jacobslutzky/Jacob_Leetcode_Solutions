class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 != 0:
            return False
        half_sum = sum(nums)//2

        dp = [False]*(half_sum+1)
        dp[0] = True
        nums.sort()
    
        for num in nums:
            for i in range(half_sum,num-1,-1):
                if dp[i-num]:
                    dp[i] = True
        return dp[-1]



