class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0
        for i in range(0, len(nums)):
            currentSum += nums[i]
            maxSub = max(currentSum, maxSub)
            if currentSum <= 0:
                currentSum = 0
        return maxSub
            
            