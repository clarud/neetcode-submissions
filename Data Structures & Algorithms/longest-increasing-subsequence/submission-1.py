class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [None] * n

        def dp(i):
            if memo[i] is not None:
                return memo[i]
            best = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(best, dp(j) + 1)
            memo[i] = best
            return best

        return max(dp(x) for x in range(n))