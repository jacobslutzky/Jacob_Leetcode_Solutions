class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            if grid[row][0] == 0:
                for col in range(len(grid[0])):
                    grid[row][col] = int(not grid[row][col])
        print(grid)
        for col in range(1, len(grid[0])):
            count_zeros = 0
            count_ones = 0
            for row in range(len(grid)):
                if grid[row][col]==1:
                    count_ones+=1
                else:
                    count_zeros+=1
            if count_zeros > count_ones:
                for row in range(len(grid)):
                    grid[row][col] = int(not grid[row][col])
        count = 0
        for row in grid:
            count += int(("").join(map(str, row)),2)
        return count
            
