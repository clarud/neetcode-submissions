class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        stack = deque()
        res = 0
        for ch in s:
            if ch in dup:
                while ch in stack:
                    stack.popleft()
                dup = set(stack)
            dup.add(ch)
            stack.append(ch)
            res = max(res, len(dup))
        return res