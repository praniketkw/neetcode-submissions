class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        nums.sort()

        def dfs(total):
            if total in dp:
                return dp[total]
            
            res = 0
            for i in range(len(nums)):
                if total<nums[i]:
                    break
                res += dfs(total-nums[i])
                
            dp[total] = res
            return dp[total]

        return dfs(target)
            


