class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            adj[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs]==[]:
                True
            
            visit.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

