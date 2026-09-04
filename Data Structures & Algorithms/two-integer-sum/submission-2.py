class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = [target - num for num in nums]
        for i, num in enumerate(diff):
            if num in nums:
                if i == nums.index(num):
                    continue
                return sorted([i, nums.index(num)])
        return [-1, -1]