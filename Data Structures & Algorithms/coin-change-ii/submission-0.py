class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, total):
            if (i,total) in dp:
                return dp[(i,total)] 
            if total==amount:
                return 1
            if total>amount or i==len(coins):
                return 0
            
            dp[i, total] = dfs(i, total+coins[i]) + dfs(i+1, total)
            return dp[(i,total)]
        
        return dfs(0,0)