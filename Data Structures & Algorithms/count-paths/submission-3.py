class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m,n
        dp = {(m-1, n-1):1}

        def dfs(r,c):
            if (min(r,c)<0 or r>=rows or c>=cols):
                return 0
            if r==m-1 and c==n-1:
                return 1
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = dfs(r,c+1) + dfs(r+1,c)
            return dp[(r,c)]
        
        return dfs(0,0)