class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        l = 0
        res = 0
        dup = set()
        for r in range(len(s)):
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[r])
            res = max(res, r - l + 1)
        return res
        