import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            diff = abs(stone1 - stone2)
            if diff == 0:
                continue
            else:
                heapq.heappush(heap, -diff)
        if heap:
            return -heap[0]
        else:
            return 0