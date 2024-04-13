class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for x in range(len(heights)+1):
            while stack and (x==len(heights) or heights[x] <= stack[-1][1]):
                x_to_remove, height_to_remove = stack.pop()
                old_x = -1
                if stack:
                    old_x = stack[-1][0]
                print("x: " + str(x-1) + " old_x: " + str(old_x) + " height:" + str(height_to_remove))
                print((x-1-old_x)*height_to_remove)
                maxArea = max(maxArea, (x-1-old_x)*height_to_remove)
            print()
            if x < len(heights):
                stack.append((x,heights[x]))
            
            
                
        return maxArea