class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for i, num in enumerate(nums_set):
            if num - 1 not in nums_set:
                tempres = 0
                temp = num
                while temp in nums_set:
                    tempres += 1
                    temp += 1
                if tempres > res:
                    res = tempres
        return res