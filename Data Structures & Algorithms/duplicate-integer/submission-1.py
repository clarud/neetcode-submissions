class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            if counter[num] == 1:
                return True
            counter[num] += 1
        return False
