class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        i = 0
        t = 0
        while i < len(count):

            if count[i] == 0:
                i += 1
                continue
            nums[t] = i
            count[i] -= 1
            t += 1

