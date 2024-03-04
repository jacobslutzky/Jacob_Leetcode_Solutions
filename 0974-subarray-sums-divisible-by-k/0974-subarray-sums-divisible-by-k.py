class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        

        prefix_sum = {0:1}
        count = 0
        rolling_sum = 0
        for i in range(len(nums)):
            rolling_sum += nums[i]
            rolling_sum = rolling_sum % k
            
            if (rolling_sum) in prefix_sum:
                count += prefix_sum[rolling_sum]
                prefix_sum[rolling_sum] += 1
            else:
                prefix_sum[rolling_sum] = 1
        return count