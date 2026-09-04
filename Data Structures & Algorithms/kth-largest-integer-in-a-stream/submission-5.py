class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.sortednums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        k = self.k
        self.nums.append(val)
        self.sortednums.append(val)
        self.sortednums.sort()
        if k <= len(self.sortednums):
            return self.sortednums[-k]
        else:
            return self.sortednums[-1]
        




        
