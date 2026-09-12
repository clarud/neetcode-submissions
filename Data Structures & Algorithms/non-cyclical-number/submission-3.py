class Solution:
    def isHappy(self, n: int) -> bool:
        curr = 0
        seen = set()
        new = str(n)
        while True:
            for ch in new:
                curr += int(ch) ** 2
            if curr == 1:
                return True
            if curr != 0 and curr in seen:
                break
            seen.add(curr)
            new = str(curr)
            curr = 0
        return False
            
    