class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        
        low, high = 0, (h * w) - 1
        
        while low <= high:
            mid = low + (high - low) // 2

            i = mid // w
            j = mid % w

            print(mid, i, j)

            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False