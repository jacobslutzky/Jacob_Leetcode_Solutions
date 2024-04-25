class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        left = -1
        output = []
        while top < bottom and left < right:
            for i in range(left+1, right):
                output.append(matrix[top][i])
            right-=1
            
            if left == right:
                break

            for j in range(top+1, bottom):
                output.append(matrix[j][right])
            bottom-=1
            
            if top == bottom:
                break
           
            for i in range(right-1, left, -1):
                output.append(matrix[bottom][i])
            left += 1
            
            if left == right:
                break

            for j in range(bottom-1, top, -1):
                output.append(matrix[j][left])
            top += 1
           
        return output