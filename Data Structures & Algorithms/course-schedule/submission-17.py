class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0]*numCourses
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            ind[pre]+=1
            adj[crs].append(pre)
        
        q = deque()
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)
        
        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            for pre in adj[node]:
                ind[pre]-=1
                if ind[pre]==0:
                    q.append(pre)
        
        return finish == numCourses



