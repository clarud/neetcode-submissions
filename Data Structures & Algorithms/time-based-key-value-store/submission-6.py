class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        curr = self.store[key]
        lo, hi = 0, len(curr) - 1
        res = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if curr[mid][1] <= timestamp:
                res = curr[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        return res

