import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Correct the range for 1-based indexing
        adj = {i: [] for i in range(1, n + 1)}

        for u, v, t in times:
            adj[u].append([v, t])
        
        res = {}
        minheap = [(0, k)] # (time, node)

        while minheap:
            t1, n1 = heapq.heappop(minheap)
            if n1 in res:
                continue
            res[n1] = t1
            
            for n2, t2 in adj[n1]:
                if n2 not in res:
                    heapq.heappush(minheap, (t1 + t2, n2))
        
        # 2. Check all nodes from 1 to n
        if len(res) < n:
            return -1
            
        return max(res.values())