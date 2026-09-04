class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dp(index):
            if index >= len(s):
                return True
            if index in memo:
                return memo[index]
            for word in wordDict:
                if index + len(word) <= len(s) and s[index: index + len(word)] == word:
                    if dp(index + len(word)):
                        memo[index] = True
                        return memo[index]
            memo[index] = False
            return False

        return dp(0)