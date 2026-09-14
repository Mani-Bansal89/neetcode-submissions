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

        while queue:
            curr = queue.popleft()
            i, j, minutes = curr[0], curr[1], curr[2]

            for x in range(2):
                for y in range(2):
                    dx = edge_i[x][y]
                    dy = edge_j[x][y]
                    if 0 <= i + dx < n and 0 <= j + dy < m and grid[i+dx][j+dy] == 1:
                        grid[i+dx][j+dy] = 2
                        queue.append([i+dx, j+dy, minutes + 1])
    
          
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1      
        return minutes 

