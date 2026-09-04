class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            target = -nums[i]
            l, r  = i + 1, len(nums) - 1
            while l < r:
                now = nums[l] + nums[r]
                if now == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                        
                    
                    while l < r - 1 and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                elif now > target:
                    r -= 1
                else:
                    l += 1
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
            i += 1

        return res