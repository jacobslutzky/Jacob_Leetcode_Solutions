class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for element in row] for row in board]
        def dfs(row,col,word):
            if not word:
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if word[0] != board[row][col] or visited[row][col]:
                return False
            visited[row][col] = 1
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                if dfs(row+i,col+j,word[1:]):
                    return True
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col,word):
                    return True
        return False