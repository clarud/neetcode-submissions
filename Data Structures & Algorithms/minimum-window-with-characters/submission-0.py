class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if t == "":
            return ""
        l = r = 0
        tcount = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(tcount)
        res, resLen = [-1, -1], float("inf")
        while r < len(s):
            window[s[r]] += 1
            if s[r] in tcount and window[s[r]] == tcount[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = res 
        return s[l:r + 1] if resLen != float("inf") else ""
