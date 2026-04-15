class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        
        i = 1
        while i*i<=n:
            squares.append(i*i)
            i+=1
        
        dp = [n+1]*(n+1)
        dp[0] = 0

        for a in range(1,n+1):
            for s in squares:
                if a-s>=0:
                    dp[a] = min(dp[a], 1+dp[a-s])
        
        return dp[n]


