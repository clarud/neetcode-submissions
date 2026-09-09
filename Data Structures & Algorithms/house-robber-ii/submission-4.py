class Solution:
    def rob(self, nums: List[int]) -> int:
        # let dp[i][j] = maximum amount of money that can be robbed after i house given j whether first house is robbed
        n = len(nums)
        if n == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        one = nums[0]
        two = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = two
            two = max(two, nums[i] + one)
            one = tmp

        return max(two, one)

