class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return -1
        nums.sort(reverse=True)
        return ((nums[0] * nums[1]) - (nums[-1] * nums[-2]))