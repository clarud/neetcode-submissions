class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r  = i + 1, len(nums) - 1
            while l < r:
                now = nums[l] + nums[r] + num
                if now == 0:
                    res.append([num, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif now > 0:
                    r -= 1
                else:
                    l += 1
        return res