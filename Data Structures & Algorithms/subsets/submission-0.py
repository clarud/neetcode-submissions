class Solution:
    def helper(self, index: int, curr: List[int]) -> None:
        if index >= len(self.nums):
            self.res.append(curr[:])
            return
        curr.append(self.nums[index])
        self.helper(index + 1, curr[:])
        curr.pop()
        self.helper(index + 1, curr[:])
        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.helper(0, [])
        return self.res