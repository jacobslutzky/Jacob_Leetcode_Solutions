class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height)-1
        max_water = 0
        while low < high:
            max_water = max(max_water, (high-low)*min(height[high],height[low]))
            
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_water