class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[-1]
        l = 1
        r = len(height)-2
        count = 0
        while l <= r:
            left_max = max(left_max,height[l])
            right_max = max(right_max, height[r])

            if left_max <= right_max:
                count += left_max-height[l]
                l+=1
            else:
                count += right_max-height[r]
                r-=1
        return count