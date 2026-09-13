class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, e, c in times:
            adj[s].append((e, c))
        
        costs = [float("inf")] * (n + 1)
        costs[k] = 0

        q = deque([k])
        while q:
            node = q.popleft()

            for nextnode, cost in adj[node]:
                if costs[node] + cost < costs[nextnode]:
                    costs[nextnode] = costs[node] + cost
                    q.append(nextnode)
                    
        max_time = max(costs[1:])
        return max_time if max_time != float("inf") else -1

        
