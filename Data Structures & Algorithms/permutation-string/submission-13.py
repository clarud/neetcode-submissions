class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        for j, s in enumerate(s2):
            req = Counter(s1)
            if s not in req:
                continue
            if req[s] == 0:
                continue
            count = 0
            req[s] -= 1
            for i in range(1, min(len(s1), len(s2) - j)):
                if s2[j + i] not in req or req[s2[j + i]] == 0:
                    break
                req[s2[j + i]] -= 1
                count += 1
            if count == len(s1) - 1:
                return True
        return False
                 