class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        count = Counter(nums)
        buckets = [[] for i in range(max(count.values()))]
        for key, value in count.items():
            buckets[value - 1].append(key)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
            if len(res) == k:
                return res
        return res