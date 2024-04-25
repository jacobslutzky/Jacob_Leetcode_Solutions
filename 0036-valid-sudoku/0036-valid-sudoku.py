class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        squares = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val != ".":
                    if val in rows[row] or val in cols[col] or val in squares[(3*(row//3))+(col//3)]:

                        return False
                    rows[row].add(val)
                    cols[col].add(val)
                    squares[(3*(row//3))+(col//3)].add(val)
        return True