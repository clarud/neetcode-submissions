class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[amt] is the min coins used to achieve remaining amt
        cache = [amount + 1] * (amount + 1)
        def helper(q):
            if q == 0:
                return 0
            if q < 0:
                return amount + 1
            if cache[q] != amount + 1:
                return cache[q]
            cache[q] = min([helper(q - coin) + 1 for coin in coins])
            return cache[q]
        res = helper(amount)
        return res if res < amount + 1 else -1
        


            