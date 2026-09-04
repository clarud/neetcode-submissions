class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        stack.append((0 ,[], 0))
        while stack:
            start, curr, val = stack.pop()
            if val == target:
                res.append(curr)
            if val > target:
                continue
            for i in range(start, len(nums)):
                stack.append((i, curr + [nums[i]], val + nums[i]))
        return res




