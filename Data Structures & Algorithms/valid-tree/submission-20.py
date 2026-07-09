class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(i,par):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j==par:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        
        return dfs(0,-1) and len(visit)==n



                

