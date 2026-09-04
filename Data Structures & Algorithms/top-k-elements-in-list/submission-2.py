class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        count = [(-num, key) for key, num in Counter(nums).items()]
        heapq.heapify(count)

        return [x[1] for x in heapq.nsmallest(k, count)]