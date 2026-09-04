class Solution:
    def helper(self, nums, i):
        if i >= (len(nums) - 1):
            return True
        if nums[i] == 0:
            return False
        return True in [self.helper(nums, i + n) for n in range(1, nums[i] + 1)]

    def canJump(self, nums: List[int]) -> bool:
        return self.helper(nums, 0)
