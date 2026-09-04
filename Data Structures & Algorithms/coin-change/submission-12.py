class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[amt] is the min coins used to achieve remaining amt
        visited = [False] * (amount + 1)
        q = deque()
        q.append((0, 0))
        while q:
            amt, i = q.popleft()
            for c in coins:
                if amt + c == amount:
                    return i + 1
                if amt + c < amount and not visited[amt + c]:
                    q.append((amt + c, i + 1))
                    visited[amt + c] = True
        return -1 if amount > 0 else 0
        


            