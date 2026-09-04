class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] be the number of distinct way to reach i step
        before1 = 1
        before2 = 1
        for i in range(2, n + 1):
            now = before1 + before2
            before2 = before1
            before1 = now
        return before1
