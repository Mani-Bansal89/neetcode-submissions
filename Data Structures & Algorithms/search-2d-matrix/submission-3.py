class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        up, left = 0, 0
        down, right = m - 1, n - 1
        mid = (up + down) // 2

        while left <= right :
            while up <= down :
                mid = (up + down) // 2
                if matrix[mid][left] < target:
                    up = mid + 1
                elif matrix[mid][left] > target:
                    down = mid - 1
                else:
                    return True
                
            mid = (left + right) // 2
            if matrix[down][mid] < target:
                left = mid + 1
            elif matrix[down][mid] > target:
                right = mid - 1
            else:
                return True
            
        return False