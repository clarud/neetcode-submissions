class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random
        def qsort(arr: List[int]):
            if not arr:
                return []
            partition = random.randint(0, len(arr) - 1)
            pivot = arr[partition]
            left = []
            mid = []
            right = []
            for num in arr:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    mid.append(num)
            return qsort(left) + mid + qsort(right)
        return qsort(nums)

