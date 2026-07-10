class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = {amount:0}
        def dfs(total):
            if total in dp:
                return dp[total]
            
            res = float("inf")
            for coin in coins:
                if total+coin<=amount:
                    res = min(res, 1+dfs(total+coin))
                else:
                    break
            
            dp[total] = res
            return dp[total]
        
        ans = dfs(0)
        return ans if ans!=float("inf") else -1

                