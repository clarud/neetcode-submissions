class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] be the number of distinct way to reach i step
        cache = [-1] * (n + 1)
        def dfs(i):
            if i <= 1:
                return 1
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i - 1) + dfs(i - 2)
            return cache[i]
        return dfs(n)
