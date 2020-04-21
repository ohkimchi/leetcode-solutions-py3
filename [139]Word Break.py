class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i, n):
                if dp[i] and s[i:j + 1] in wordDict:
                    dp[j + 1] = True
        return dp[-1]
