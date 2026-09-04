class Solution:
    def binarySearch(self, arr: List[int], target: int) -> bool:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return self.binarySearch(matrix[mid], target)
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
