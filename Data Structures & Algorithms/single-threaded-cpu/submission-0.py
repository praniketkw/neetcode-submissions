class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda x:x[0])
        
        minheap = []
        cpu = tasks[0][0]
        i = 0
        res = []

        while minheap or i<len(tasks):
            while i<len(tasks) and tasks[i][0]<=cpu:
                s,p,idx = tasks[i]
                heapq.heappush(minheap, (p,idx))
                i+=1
            if minheap:
                chosen_p, chosen_i = heapq.heappop(minheap)
                res.append(chosen_i)
                cpu+=chosen_p
            else:
                nextstart = tasks[i][0]
                cpu = nextstart
        return res
            
                







