class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        start, end = 0, len(tmp) - 1
        
        while start < end:
            if tmp[start] != tmp[end]:
                return False
            start += 1
            end -= 1
        return True