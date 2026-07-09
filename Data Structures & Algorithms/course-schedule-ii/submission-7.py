class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre]+=1
        
        res = []
        q = deque()

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        finish = 0

        while q:
            node = q.popleft()
            finish+=1
            res.append(node)

            for pre in adj[node]:
                indegree[pre]-=1
                if indegree[pre]==0:
                    q.append(pre)
        
        return res[::-1] if finish==numCourses else []


            

