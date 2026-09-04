class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        add = 0
        prefix = []
        prefix.append(add)
        for num in nums:
            add += num
            prefix.append(add)
        print(prefix)
        res = float("inf")
        for i in range(len(nums)):
            l, r = i + 1, len(nums)
            curr = -1
            while l <= r:
                m = (l + r) // 2
                if prefix[m] - prefix[i] >= target:
                    curr = m
                    r = m - 1
                else:
                    l = m + 1
            if curr == -1:
                continue
            else:
                res = min(res, curr - i)
        return res if res != float("inf") else 0

                    
