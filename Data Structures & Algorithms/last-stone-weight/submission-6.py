class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        for i, s in enumerate(stones):
            stones[i] = -s
        heapq.heapify(stones)
        while len(stones) > 1:
            rock1, rock2 = heapq.heappop(stones), heapq.heappop(stones)
            print(rock1)
            print(rock2)
            if rock1 == rock2:
                continue
            else:
                heapq.heappush(stones, -(rock2 - rock1))
        return abs(heapq.heappop(stones)) if stones else 0


