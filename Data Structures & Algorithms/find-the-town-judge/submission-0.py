class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {i:[] for i in range(1,n+1)}

        for u,v in trust:
            adj[u].append(v)
        
        count = 0
        leader = 0
        for node,vals in adj.items():
            if not vals:
                leader = node
                count+=1

        if leader==0 or count>1:
            return -1
        
        for vals in adj.values():
            if vals and leader not in vals:
                return -1
        
        return leader
