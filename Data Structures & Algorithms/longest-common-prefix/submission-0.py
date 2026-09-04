class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return ""
        for ch in strs[0]:
            curr = res + ch
            if all(curr == st[:len(curr)] for st in strs):
                res += ch
        return res
