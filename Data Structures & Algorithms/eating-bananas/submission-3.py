class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(x):
            res = 0
            for p in piles:
                res += math.ceil(p/x)
            return res
        l, r = 1, max(piles)
        res = -1
        while l <= r:
            m = (l + r) // 2
            if eat(m) <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
