class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        cycle = set()
        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



