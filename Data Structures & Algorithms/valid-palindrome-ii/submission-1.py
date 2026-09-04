class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        for i, c in enumerate(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if l < len(s) - 1 and l == i:
                    l += 1
                if r > 0 and r == i:
                    r -= 1
                if s[l] != s[r]:
                    count += 1
                    break
                l += 1
                r -= 1
        return True if count < len(s) else False
