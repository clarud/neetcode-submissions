class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = (0, 0)
        for i, c in enumerate(s):
            l = r = i
            while l >= 0 and r <= len(s) - 1:
                if s[l] != s[r]:
                    break
                else:
                    if r - l >= (long[1] - long[0]):
                        long = (l, r)
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r <= len(s) - 1:
                if s[l] != s[r]:
                    break
                else:
                    if r - l >= (long[1] - long[0]):
                        long = (l, r)
                l -= 1
                r += 1
        return s[long[0]: long[1] + 1]

