class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda x:x[0])

        time = tasks[0][0]
        minheap = [] #(processing_time, idx)
        res = []
        
        i = 0

        while i<len(tasks) or minheap:
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minheap, (tasks[i][1], tasks[i][2]))
                i+=1
            
            if not minheap:
                time = tasks[i][0]
            if minheap:
                proc_time, idx = heapq.heappop(minheap)
                time+=proc_time
                res.append(idx)
        
        return res
