class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for ch in strs[0]:
            if all(res + ch in strss for strss in strs):
                res += ch
            else:
                break
        return res