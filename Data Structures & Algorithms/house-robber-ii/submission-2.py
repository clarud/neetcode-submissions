class Solution:
    def rob(self, nums: List[int]) -> int:
        # let dp[i][j] = maximum amount of money that can be robbed after i house given j whether first house is robbed
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        memo = [[-1] * 2 for i in range(n)]
        def dp(i, first):
            if i >= n or (first and i == n - 1):
                return 0
            if first and i == n - 2:
                return nums[i]
            elif i == n - 1:
                return nums[i]
            if memo[i][first] == -1:
                memo[i][first] = max(dp(i + 1, first), nums[i] + dp(i + 2, first))

            return memo[i][first]
            
        return max(dp(0, True), dp(1, False))