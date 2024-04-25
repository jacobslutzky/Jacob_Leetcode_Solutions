class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(row, col):
            if row < 0 or col<0 or row >= len(board) or col >= len(board[0]) or board[row][col] != "O":
                return
            board[row][col] = "Y"
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(row+i,col+j)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)

        for j in range(len(board[0])):
            dfs(0,j)
            dfs(len(board)-1,j)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "Y":
                    board[row][col] = "O"
        
        

                