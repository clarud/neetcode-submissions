class Solution:
    def helper(self, index: int, tot: int, arr: List[int]):
        if tot > self.target:
            return
        if tot == self.target:
            self.res.append(arr)
        for i in range(index, len(self.nums)):
            arr.append(self.nums[i])
            self.helper(i, tot + self.nums[i], arr[:])
            arr.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.nums = nums
        self.res = []
        self.helper(0, 0, [])
        return self.res