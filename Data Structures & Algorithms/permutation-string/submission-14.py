class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s2) < len(s1):
            return False
        s1_freq = Counter(s1)
        window_freq = Counter(s2[:len(s1)])
        if s1_freq == window_freq:
                return True
        for i in range(len(s1), len(s2), 1):
            window_freq[s2[i - len(s1)]] -= 1
            if s2[i] not in window_freq:
                window_freq[s2[i]] == 1
            window_freq[s2[i]] += 1
            if s1_freq == window_freq:
                return True
        return False
            
