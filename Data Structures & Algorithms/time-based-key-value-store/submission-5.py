class TimeMap:

    def __init__(self):
        self.val = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.val[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.val[key]
        # find maximum < timestamp:
        if not arr:
            return ""
        res = ""
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2 
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                res = arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return res