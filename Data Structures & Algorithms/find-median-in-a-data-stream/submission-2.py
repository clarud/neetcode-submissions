import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.middle = None
        self.right = []

    def addNum(self, num: int) -> None:
        if self.middle is None:
            if not self.right or num < self.right[0]:
                heapq.heappush(self.left, -num)
                self.middle = -heapq.heappop(self.left)
            else:
                heapq.heappush(self.right, num)
                self.middle = heapq.heappop(self.right)
        else:
            if num < self.middle:
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, self.middle)
            else:
                heapq.heappush(self.left, -self.middle)
                heapq.heappush(self.right, num)
            self.middle = None


        

    def findMedian(self) -> float:
        if self.middle is not None:
            return self.middle
        else:
            low = -self.left[0]
            high = self.right[0]
            return (high + low) / 2