import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = 0
        col = 0
        for row in range(math.ceil(len(matrix)/2)):
            for col in range(row, len(matrix[0])-row-1):
                print(str(row) + " " + str(col))
                #print(matrix)
                prev = matrix[row][col]
                for i in range(4):
                    row, col = col, len(matrix[0])-1-row
                    temp = matrix[row][col]
                    matrix[row][col] = prev
                    prev = temp
        print(matrix)