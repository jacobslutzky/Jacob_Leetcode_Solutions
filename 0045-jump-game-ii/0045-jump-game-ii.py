class Solution:
    def jump(self, nums: List[int]) -> int:
        dp =[float("inf")]*len(nums)
        dp[0] = 0
        farthest = 0
        count = 0
        end = 0
        for i in range(0, len(nums)-1):
            farthest = max(i + nums[i], farthest)
            
            if i == end:
                end = farthest
                count+=1
        return count




        