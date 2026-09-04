class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i, num in enumerate(nums):
            need = target - num
            if num in needs:
                if needs[num] < i:
                    return [needs[num], i]
                else:
                    return [i, needs[num]]
            needs[need] = i
        return [-1, -1]

