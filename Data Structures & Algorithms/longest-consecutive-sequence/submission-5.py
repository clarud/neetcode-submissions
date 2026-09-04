class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in hashset:
                continue
            curr = 1
            val = num
            while val + 1 in hashset:
                curr += 1
                val += 1      
            longest = max(curr, longest)
        return longest

            