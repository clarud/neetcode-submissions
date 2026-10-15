class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = 0, len(nums) // 2
        res = []
        while right < len(nums):
            res.append(nums[left])
            res.append(nums[right])
            left += 1
            right += 1
        return res
