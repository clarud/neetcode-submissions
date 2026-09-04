import heapq
from collections import Counter
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        flip = [(-y, x, 0) for x, y in freq.items()]
        heapq.heapify(flip)
        idle = deque()
        i = 0
        while flip or idle:
            while idle and idle[0][2] <= i:
                heapq.heappush(flip, idle.popleft())
            if not flip:
                i += 1
                continue
            count, val, time = heapq.heappop(flip)
            if count + 1 < 0:
                idle.append((count+ 1, val, i + n + 1))
            i += 1
        return i