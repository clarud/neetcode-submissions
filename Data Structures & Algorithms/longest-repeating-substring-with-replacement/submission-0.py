class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        length = len(s)
        res = 0
        for ch in charset:
            count = l = 0
            for r in range(length):
                if s[r] == ch:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == ch:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res
                    
