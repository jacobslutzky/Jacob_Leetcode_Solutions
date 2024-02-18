class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        while i < len(nums)-2:
            low = i+1
            high = len(nums)-1
            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    output.append([nums[i],nums[low],nums[high]])
                
                    while low < len(nums)-1 and nums[low] == nums[low+1]:
                        low += 1
                    while high > 0 and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1  
                    
                elif nums[i] + nums[low] + nums[high] < 0:
                    low+=1
                else:
                    high -= 1
            
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        
        return output