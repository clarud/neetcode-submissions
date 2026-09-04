class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s2) < len(s1):
            return False
        s1_freq = [0] * 26
        window_freq = [0] * 26
        for s in s1:
            s1_freq[ord(s) - 97] += 1
        for s in s2[:len(s1)]:
            window_freq[ord(s) - 97] += 1

        if s1_freq == window_freq:
                return True
        for i in range(len(s1), len(s2), 1):
            window_freq[ord(s2[i - len(s1)]) - 97] -= 1
            window_freq[ord(s2[i]) - 97] += 1
            if s1_freq == window_freq:
                return True
        return False
            
