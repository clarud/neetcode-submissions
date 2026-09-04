
class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed = ""
        for st in s:
            if st.isalnum():
                removed += st.lower()
        for i in range(len(removed) // 2):
            if removed[i] != removed[len(removed) - 1 - i]:
                return False
        return True