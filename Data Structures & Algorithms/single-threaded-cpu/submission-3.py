class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        
        tasks.sort()

        res = []
        minheap = []
        time = tasks[0][0]
        i = 0

        while minheap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i+=1
            
            if not minheap:
                time = tasks[i][0]
            else:
                proctime, idx = heapq.heappop(minheap)
                time+=proctime
                res.append(idx)
        
        return res


