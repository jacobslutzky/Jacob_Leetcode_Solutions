class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        self.maxPath = 0
        def dfs(row,col,currPathSum):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or visited[row][col] or grid[row][col]==0:
                return

            currPathSum += grid[row][col]
            self.maxPath = max(self.maxPath,currPathSum)
            visited[row][col] = True

            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(row+i,col+j,currPathSum)

            visited[row][col] = False
            
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i,j,0)
                print(grid[i][j], self.maxPath)
        return self.maxPath