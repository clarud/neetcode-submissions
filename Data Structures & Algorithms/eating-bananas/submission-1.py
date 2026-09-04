class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def test(k):
            sets = 0
            for pile in piles:
                sets += math.ceil(float(pile)/k)
            return sets
        while left <= right:
            mid = (left + right) // 2
            if test(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
