import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if self.k <= len(self.nums):
            return heapq.nlargest(self.k, self.nums)[-1]
        else:
            return heapq.nlargest(1, self.nums)[-1]
        




        
