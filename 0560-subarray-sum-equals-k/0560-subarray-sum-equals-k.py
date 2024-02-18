class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        prefSum = {0:1}
    
        running_sum = 0
        for i in range(len(nums)):
            running_sum+=nums[i]
            if running_sum-k in prefSum:
                count += prefSum[running_sum-k]
            
            if running_sum in prefSum:
                prefSum[running_sum] +=1
            else: 
                prefSum[running_sum] = 1
        return count

            
