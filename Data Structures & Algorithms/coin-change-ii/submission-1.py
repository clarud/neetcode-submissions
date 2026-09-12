class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[None] * (amount + 1) for _ in range(n)]
        def dfs(i, rem):
            if i == n:
                return 0
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            if memo[i][rem] is not None:
                return memo[i][rem]
            memo[i][rem] = dfs(i, rem - coins[i]) + dfs(i + 1, rem)
            return memo[i][rem]

        return dfs(0, amount)