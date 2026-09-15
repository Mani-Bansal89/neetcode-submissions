class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        n = len(image)
        m = len(image[0])
        
        og_color = image[sr][sc]
        visited = {}
        queue.append((sr, sc))
        image[sr][sc] = color
        
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            sr = curr[0]
            sc = curr[1]
            
            for (i, j) in [(0, 1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= sr+i < n and 0 <= sc+j < m and image[sr+i][sc+j] == og_color and (sr + i, sc + j) not in visited:
                        queue.append((sr + i, sc + j))
                        image[sr + i][sc + j] = color

        return image 


        