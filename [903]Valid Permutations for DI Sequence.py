class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        m = 10 ** 9 + 7
        for i in range(1, n + 1):
            for j in range(0, i + 1):
                if S[i - 1] == 'D':
                    for k in range(j, i):
                        dp[i][j] = dp[i][j] % m + dp[i - 1][k] % m
                else:
                    for k in range(0, j):
                        dp[i][j] = dp[i][j] % m + dp[i - 1][k] % m
        res = 0
        for i in range(0, n + 1):
            res = res % m + dp[n][i] % m
        return res % m
