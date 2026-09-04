class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        count = [(-num, key) for key, num in Counter(nums).items()]
        heapq.heapify(count)
        res = []
        for i in range(k):
            freq, largest_key = heapq.heappop(count)
            res.append(largest_key)
        return res