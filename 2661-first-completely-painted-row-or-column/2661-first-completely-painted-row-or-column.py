class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        d = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                d[mat[row][col]] = [row,col]
        rows = [len(mat[0])]*len(mat)
        cols = [len(mat)]*len(mat[0])
        for i in range(len(arr)):
            row, col = d[arr[i]]
            rows[row] -= 1
            cols[col]-=1
            if rows[row] == 0 or cols[col] == 0:
                return i