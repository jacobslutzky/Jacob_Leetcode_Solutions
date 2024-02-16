class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height)-1
        max_height = 0
        i = 0
        while low < high:
            max_height = max(min(height[low],height[high])*(high-low),max_height)
            if height[low] <= height[high]:
                low +=1
            else:
                high-=1
        return max_height