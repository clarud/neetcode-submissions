class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer approach since it is sorted
        first, second = 0, len(numbers) - 1
        if len(numbers) < 2:
            return [-1, -1]
        while first < second:
            curr = numbers[first] + numbers[second]
            if curr > target:
                second -= 1
            elif curr < target:
                first += 1
            else:
                return [first + 1, second + 1]
        return [-1, -1]