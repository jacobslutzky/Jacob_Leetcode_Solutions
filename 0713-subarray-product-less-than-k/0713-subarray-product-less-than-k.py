class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        count = 0
        curr_product = 1
        while end < len(nums):
            if curr_product * nums[end] < k:
                curr_product *= nums[end]
                count += end-start+1
                end+=1
            else:
                if end == start:
                    end+=1
                else:
                    curr_product /= nums[start]
                start += 1
            print(curr_product)
          
        return count