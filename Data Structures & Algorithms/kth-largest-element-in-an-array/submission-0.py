import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        inverse = [-x for x in nums]
        heapq.heapify(inverse)
        return -heapq.nsmallest(k, inverse)[k - 1]