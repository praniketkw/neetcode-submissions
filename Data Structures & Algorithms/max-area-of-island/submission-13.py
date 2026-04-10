class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows,cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,-1], [0,1]]

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            area = 1
            grid[r][c]=0

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if (min(nr,nc)<0 or nr>=rows or nc>=cols or grid[nr][nc]==0):
                        continue
                    
                    area+=1
                    grid[nr][nc]=0
                    q.append((nr,nc))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    res = max(res, bfs(r,c))
        
        return res