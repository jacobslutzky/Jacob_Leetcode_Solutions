class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = [[[0,0] for j in row] for row in heights]

        def dfs(row,col,is_pac):
            visited[row][col][is_pac] = 1
            
            for i, j in [[-1,0],[1,0],[0,-1],[0,1]]:
                new_row = row+i
                new_col = col+j
                if new_row >= 0 and new_col>=0 and new_row < len(heights) and new_col < len(heights[0]):
                    if heights[new_row][new_col] >= heights[row][col] and not visited[new_row][new_col][is_pac]:
                        dfs(new_row,new_col,is_pac)
  
        for i in range(len(heights)):
            dfs(i,0,1)
            dfs(i,len(heights[0])-1,0)
        for j in range(len(heights[0])):
            dfs(0,j,1)
            dfs(len(heights)-1,j,0)
     
        output = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if visited[row][col][0] and visited[row][col][1]:
                    output.append([row,col])
        return output