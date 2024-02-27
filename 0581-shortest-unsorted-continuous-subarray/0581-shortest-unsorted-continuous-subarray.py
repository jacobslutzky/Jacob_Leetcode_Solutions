class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums)-1 and nums[start] <= nums[start+1]:
            start+=1
        if start == len(nums)-1:
            return 0

        end = len(nums)-1
        while end > 0 and nums[end] >= nums[end-1]:
            end-=1

        max_elem = max(nums[start:end+1])
        min_elem = min(nums[start:end+1])
        print(start)
        print(end)
        
        new_end = end
        new_start= start
        for i in range(end+1,len(nums)):
            if nums[i] < max_elem:
                new_end+=1
            else:
                break
        for i in range(start-1,-1,-1):
            if nums[i] > min_elem:
                new_start-=1
            else:
                break


        return new_end-new_start+1