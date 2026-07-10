class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text2), len(text1)

        dp = [[0 for i in range(cols+1)] for j in range(rows+1)]

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if text2[r]==text1[c]:
                    dp[r][c] = 1+dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]
