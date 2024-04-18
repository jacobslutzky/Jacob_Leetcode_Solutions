class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        graph = {}
        destination = len(board)**2

        forward = 1
        col = 0
        i = 1
        
        for row in range(len(board)-1,-1,-1):
            while col < len(board[0]) and col >= 0:
                graph[i] = (row,col)
                i+=1
                col += forward
            col -= forward
            forward*=-1
        
        queue = [1]
        iteration_num = 0
        visited = [0]*(destination+1)
        visited[1] = 1
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                n = queue.pop(0)
                if n == destination:
                    return iteration_num
                
                for new_n in range(n+1, min(destination,n+6)+1):
                    row, col = graph[new_n]
                    if board[row][col] != -1:
                        new_n = board[row][col]
                    if not visited[new_n]:
                        visited[new_n] = 1
                        queue.append(new_n)
                    
            iteration_num+=1
        return -1