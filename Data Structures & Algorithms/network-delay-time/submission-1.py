class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, e, c in times:
            adj[s].append((e, c))
        
        costs = [float("inf")] * (n + 1)

        min_heap = []
        heapq.heappush(min_heap, (0, k))

        while min_heap:
            time, curr = heapq.heappop(min_heap)
            if costs[curr] != float("inf"):
                continue

            costs[curr] = time

            for nextnode, weight in adj[curr]:
                if costs[nextnode] == float("inf"):
                    new_time = time + weight
                    heapq.heappush(min_heap, (new_time, nextnode))

        max_time = max(costs[1:])
        return max_time if max_time != float("inf") else -1