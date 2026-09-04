class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        def helper(remain):
            if not remain:
                res.append(stack[:])
                return
            stack.append(remain[0])
            helper(remain[1:])
            stack.pop()
            helper(remain[1:])
        helper(nums)
        return res