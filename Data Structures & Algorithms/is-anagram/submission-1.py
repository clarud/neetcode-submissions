class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(t)
        if len(s) != len(t):
            return False

        for key in s_counter:
            if key in s_counter and key in t_counter:
                if s_counter[key] != t_counter[key]:
                    return False
            else:
                return False
        return True