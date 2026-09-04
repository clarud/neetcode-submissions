class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, curr, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i, curr, remaining - nums[i])
                curr.pop()
        dfs(0, [], target)
        return res




