class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        n = len(s)
        curr = set()
        hi = 0
        while r < n:
            if s[r] not in curr:
                curr.add(s[r])
                hi = max(hi, len(curr))
                r += 1
            else:
                while s[l] != s[r]:
                    curr.remove(s[l])
                    l += 1
                curr.remove(s[l])
                l += 1
        return hi

