class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        up, left = 0, 0
        down, right = m - 1, n - 1

        while left <= right :
            while up <= down :
                if matrix[up][left] < target:
                    up += 1
                elif matrix[down][left] > target:
                    down -= 1
                else:
                    return True
            i = down
            if matrix[i][left] < target:
                left += 1
            elif matrix[i][right] > target:
                right -= 1
            else:
                return True
        return False

        
        