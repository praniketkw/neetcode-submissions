class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src,dst,time in times:
            adj[src].append([dst,time])
        
        visit = set()
        minheap = [(0,k)]
        res = 0

        while minheap:
            t1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = t1
            for n2,t2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (t1+t2,n2))
        
        return res if len(visit)==n else -1
