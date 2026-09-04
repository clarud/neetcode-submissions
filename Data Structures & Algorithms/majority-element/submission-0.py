class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        highest = (nums[0], 1)
        count = defaultdict(int)
        for i, num in enumerate(nums):
            count[num] += 1
            if count[num] > highest[1]:
                highest = (num, count[num])
        return highest[0]