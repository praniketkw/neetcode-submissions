class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                grid[row][col]=dist
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if (min(nr,nc)<0 or nr>=rows or nc>=cols or (nr,nc) in visit or grid[nr][nc]==-1):
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            dist+=1
            
        

                    

                    


        

                    
            
