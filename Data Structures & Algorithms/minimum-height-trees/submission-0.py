class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = []

        def dfs(node,parent):
            maxdepth = 0
            for child in adj[node]:
                if child==parent:
                    continue
                maxdepth = max(1+dfs(child,node),maxdepth)
            
            return maxdepth
        
        depths = []
        for i in range(n):
            depths.append([dfs(i,-1),i])

        minheight = min(depths)[0]

        for i in range(n):
            if depths[i][0]==minheight:
                res.append(depths[i][1])
        
        return res

