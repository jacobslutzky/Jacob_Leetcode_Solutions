class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i=0
        while i < len(nums)-2:
            low=i+1
            high = len(nums)-1
            while low < high:
                three_sum = nums[low] + nums[high]+nums[i]
                if three_sum > 0:
                    high-=1
                elif three_sum < 0:
                    low +=1
                else:   
                    output.append([nums[low],nums[i],nums[high]])
                    low+=1
                    high-=1
            i+=1
            while i < len(nums)-1 and nums[i] == nums[i-1]:
                i+=1
        return output