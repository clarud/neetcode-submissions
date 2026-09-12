class Solution:
    def gonext(self, n: int) -> int:
        new = str(n)
        return sum(int(ch) ** 2 for ch in new)

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.gonext(n)
        while slow != fast:
            slow = self.gonext(slow)
            fast = self.gonext(self.gonext(fast))
            if slow == 1 or fast == 1:
                return True
        return slow == 1