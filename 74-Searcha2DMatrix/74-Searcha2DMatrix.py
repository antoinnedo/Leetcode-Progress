class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search for which row to search: O(n)
        low = 0
        high = len(matrix)-1
        row = 0
        while low <= high:
            mid = low + (high-low)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                left = 0
                right = len(matrix[row])-1

                while left <= right:
                    middle = left + (right-left)//2
                    if matrix[row][middle] == target:
                        return True
                    elif matrix[row][middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1

                return False
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
