class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights), len(heights[0])
        
        minheap = [[0,0,0]] #[diff,r,c]
        visit = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while minheap:
            diff, r ,c = heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c)==(rows-1,cols-1):
                return diff
            
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if (min(nr,nc)<0 or nr>=rows or nc>=cols or (nr,nc) in visit):
                    continue
                newdiff = max(diff, abs(heights[r][c]-heights[nr][nc]))
                heapq.heappush(minheap, [newdiff,nr,nc])
        
        return 0

