class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        start = [i for i, num in enumerate(nums) if num - 1 not in nums]
        longest = 0
        for num in start:
            curr = 1
            val = nums[num]
            while val + 1 in hashset:
                curr += 1
                val += 1      
            longest = max(curr, longest)
        return longest

            