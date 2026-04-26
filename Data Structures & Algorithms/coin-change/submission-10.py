class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = {amount:0}
        
        def dfs(total):
            if total in dp:
                return dp[total]
            
            res = float("inf")
            for coin in coins:
                if total+coin>amount:
                    break
                res = min(res, 1+dfs(total+coin))
            dp[total]=res
            return dp[total]
        
        mincoins = dfs(0)
        return -1 if mincoins==float("inf") else mincoins