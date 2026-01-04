class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return self._searchRow(matrix[mid], target)
            elif target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            
        return False
    
    def _searchRow(self, row: list[int], target: int) -> bool:
        left, right = 0, len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target == row[mid]:
                return True
            elif target > row[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False
    

if __name__ == "__main__":
    solution = Solution()

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    assert solution.searchMatrix(matrix, target)

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    assert not solution.searchMatrix(matrix, target)
