class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        min, max = 0, len(matrix) - 1
        while min <= max:
            row = (min + max) // 2
            if matrix[row][-1] < target:
                min =  row + 1
            elif matrix[row][0] > target:
                max = row - 1
            else:
                break
        if not (min <= max):
            return False
        row = (min + max) // 2
        min, max = 0, len(matrix[row]) - 1
        while min <= max:
            mid = (min + max) // 2
            if target < matrix[row][mid]:
                max = mid - 1
            elif target > matrix[row][mid]:
                min = mid + 1
            else:
                return True
        return False
