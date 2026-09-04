class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] is the max amount of money after robbing house i
        # dp[i] = max of rob this house 
        before2 = 0
        before1 = 0
        for i in range(len(nums)):
            now = max(before2 + nums[i], before1)
            before2 = before1
            before1 = now
        return before1
