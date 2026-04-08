class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        row = 0
        while left <= right:
            mid = (left + right)//2 
            if matrix[mid][0] <= target:
                row = mid
                left = mid + 1
            else:
                right = mid - 1
        
        new_left, new_right = 0, len(matrix[0]) - 1
        while new_left <= new_right:
            new_mid = (new_left + new_right)//2
            if matrix[row][new_mid] == target:
                return True
            elif matrix[row][new_mid] > target:
                new_right = new_mid - 1
            else:
                new_left = new_mid + 1
        return False