class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        prefix = [[0 for i in range(len(mat[0])+1)] for row in range(len(mat)+1)]
        longest = 1
        for row in range(1,len(mat)+1):
            for col in range(1,len(mat[0])+1):
                prefix[row][col] = prefix[row][col-1] + prefix[row-1][col]-prefix[row-1][col-1]+mat[row-1][col-1]
                if row >= longest and col >= longest and prefix[row][col] - prefix[row-longest][col] - prefix[row][col-longest]+prefix[row-longest][col-longest] <= threshold:
                    longest+=1
        return longest-1
                    

