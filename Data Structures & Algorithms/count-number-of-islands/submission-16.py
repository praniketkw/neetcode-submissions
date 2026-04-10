class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c]='0'

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if (min(nr,nc)<0 or nr>=rows or nc>=cols or grid[nr][nc]=='0'):
                        continue
                    
                    grid[nr][nc]='0'
                    q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    bfs(r,c)
                    res+=1
        
        return res