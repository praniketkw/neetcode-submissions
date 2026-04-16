class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
        # dp[rows-1][cols-1] = 1

        dp = {(rows-1, cols-1):1}
        
        def dfs(r,c):
            if r==rows or c==cols or obstacleGrid[r][c]==1:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = dfs(r+1,c)+dfs(r,c+1)
            return dp[(r,c)]
        
        return dfs(0,0)

