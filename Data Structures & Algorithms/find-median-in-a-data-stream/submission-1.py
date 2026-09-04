import heapq

class MedianFinder:
    def __init__(self):
        self.left = []    # max-heap via negatives
        self.right = []   # min-heap
        self.middle = None  # holds the median when count is odd

    def addNum(self, num: int) -> None:
        # Case 1: currently even count -> we will end up with an odd count and set middle
        if self.middle is None:
            # If right is empty or num belongs to left side
            if not self.right or num <= self.right[0]:
                heapq.heappush(self.left, -num)
                self.middle = -heapq.heappop(self.left)
            else:
                heapq.heappush(self.right, num)
                self.middle = heapq.heappop(self.right)
        else:
            # Case 2: currently odd count -> we will distribute middle and num to heaps
            if num < self.middle:
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, self.middle)
            else:
                heapq.heappush(self.left, -self.middle)
                heapq.heappush(self.right, num)
            self.middle = None  # back to even count

    def findMedian(self) -> float:
        # No elements
        if self.middle is None and not self.left and not self.right:
            raise ValueError("No numbers are available")

        # Odd count
        if self.middle is not None:
            return float(self.middle)

        # Even count (peek; don't pop/mutate)
        return (-self.left[0] + self.right[0]) / 2.0
