class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = {}
        maxl = 0
        l = 0
        for i, ch in enumerate(s):
            if ch in dup:
                l = max(dup[ch] + 1, l)
            dup[ch] = i
            maxl = max(maxl, i - l + 1)
        return maxl
        