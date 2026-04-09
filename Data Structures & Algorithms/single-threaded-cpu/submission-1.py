class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda x:x[0])
        minheap = []
        res = []
        cpu = tasks[0][0]
        i = 0

        while minheap or i<len(tasks):
            while i<len(tasks) and tasks[i][0]<=cpu:
                heapq.heappush(minheap, [tasks[i][1],tasks[i][2]])
                i+=1
            if not minheap:
                cpu = tasks[i][0]
            else:
                p, idx = heapq.heappop(minheap)
                res.append(idx)
                cpu += p
        return res


            
                







