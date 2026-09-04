class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        count = Counter(nums)
        return any([c > 1 for c in count.values()])