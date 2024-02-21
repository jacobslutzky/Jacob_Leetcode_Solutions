class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
        nums = sorted(list(set(nums)))
        dp = [0 for _ in nums]
        i = 0
        while i < len(nums):
            if nums[i]-1 in d:
                dp[i] = max(dp[i-2] + d[nums[i]]*nums[i], dp[i-1])
            else:
                dp[i] = dp[i-1] + d[nums[i]]*nums[i]
            i+=1
        return dp[-1]