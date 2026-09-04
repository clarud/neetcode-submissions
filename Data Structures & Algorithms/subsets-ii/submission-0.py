class Solution:
    def helper(self, index: int, curr: List[int], nums: List[int]):
        self.res.append(curr[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            self.helper(i + 1, curr[:], nums)
            curr.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.helper(0, [], nums)
        return self.res