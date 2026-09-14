class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        minutes = 0
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i,j,0]) 

        while len(queue) != 0:
            curr = queue.popleft()
            i, j, minutes = curr[0], curr[1], curr[2]
            
            if i + 1 < n and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                queue.append([i+1, j, minutes + 1])

            if i - 1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                queue.append([i-1, j, minutes + 1])

            if j + 1 < m and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                queue.append([i, j+1, minutes + 1])

            if j - 1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2 
                queue.append([i, j-1, minutes + 1])
          
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1      
        return minutes 

