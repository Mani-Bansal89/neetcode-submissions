class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        minutes = 0
        queue = deque()
        edge_i = [[0,0],[1,-1]]
        edge_j = [[1,-1],[0,0]]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i,j,0]) 

        while len(queue) != 0:
            curr = queue.popleft()
            i, j, minutes = curr[0], curr[1], curr[2]

            for x in range(2):
                for y in range(2):
                    dx = edge_i[x][y]
                    dy = edge_j[x][y]
                    if i + dx < n and j + dy < m and i + dx >= 0 and j + dy >= 0 and grid[i+dx][j+dy] == 1:
                        grid[i+dx][j+dy] = 2
                        queue.append([i+dx, j+dy, minutes + 1])
    
          
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1      
        return minutes 

