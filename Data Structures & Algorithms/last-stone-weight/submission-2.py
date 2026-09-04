class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        neg = [-x for x in stones]
        heapq.heapify(neg)
        while len(neg) > 1:
            largest = -heapq.heappop(neg)
            slargest = -heapq.heappop(neg)
            if largest == slargest:
                continue
            else:
                heapq.heappush(neg, -(largest - slargest))
        return -heapq.heappop(neg) if neg else 0