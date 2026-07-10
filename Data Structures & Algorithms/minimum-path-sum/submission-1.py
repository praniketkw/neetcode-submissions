class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        dp = {(rows-1,cols-1): grid[rows-1][cols-1]}
        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            if r>=rows or c>=cols:
                return float("inf")
            
            res = grid[r][c]
            res+=min(dfs(r+1,c),dfs(r,c+1))
            dp[(r,c)]=res
        
            return dp[(r,c)]
        
        return dfs(0,0)
