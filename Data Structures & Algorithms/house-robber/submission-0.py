class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] is the max amount of money after robbing house i
        # dp[i] = dp[i - 2] + curr or dp[i - 1]
        # top down
        n = len(nums) - 1
        cache = [-1] * (n + 1)

        def dp(i):
            if i < 0:
                return 0
            if cache[i] != - 1:
                return cache[i]
            cache[i] = max(dp(i - 2) + nums[i], dp(i - 1))
            return cache[i]
        return dp(n)
