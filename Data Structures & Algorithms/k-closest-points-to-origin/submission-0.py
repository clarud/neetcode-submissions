import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def func(point):
            x, y = point
            return x*x + y*y
        euc_dist = [(func(x), x) for x in points]
        heapq.heapify(euc_dist)
        return [x[1] for x in heapq.nsmallest(k, euc_dist)]