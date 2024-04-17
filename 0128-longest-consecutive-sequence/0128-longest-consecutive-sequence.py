class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums:
            count = 1
            if num-1 not in nums_set:
                temp = num + 1
                while temp in nums_set:
                    count+=1
                    temp+=1
            max_count = max(max_count,count)
        return max_count

        

