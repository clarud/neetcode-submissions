class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def b_search(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return True
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return b_search(matrix[m])
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        return False