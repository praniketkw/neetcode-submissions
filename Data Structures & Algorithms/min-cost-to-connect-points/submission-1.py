class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        res = 0
        minheap = [[0,0]]
        visit = set()

        while len(visit)<len(points):
            cost, i = heapq.heappop(minheap)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            for cost1,j in adj[i]:
                if j not in visit:
                    heapq.heappush(minheap, [cost1,j])
        
        return res


