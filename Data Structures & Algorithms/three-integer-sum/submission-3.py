class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue

            low, high = i + 1, len(nums) - 1
            while low < high:
                if nums[low] + nums[high] < -num:
                    low += 1
                elif nums[low] + nums[high] > -num:
                    high -= 1
                else:
                    res.append([num, nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

        return res