class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("inf")
        for i in range(len(nums)):
            for j in range(len(nums)):
                subarray = nums[j: j + i + 1]
                maxSum = max(maxSum, sum(subarray))
        return maxSum