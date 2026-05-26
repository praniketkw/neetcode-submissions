class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(i,par):
            if i in visit:
                return False
            
            visit.add(i)
            for nei in adj[i]:
                if nei==par:
                    continue
                if not dfs(nei, i):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visit)==n


                

