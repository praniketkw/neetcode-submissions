class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        minheap = []
        curcap = 0

        for t in trips:
            numpass, start, end = t
            while minheap and minheap[0][0]<=start:
                e,p = heapq.heappop(minheap)
                curcap-=p
            curcap+=numpass
            if curcap>capacity:
                return False
            heapq.heappush(minheap, [end,numpass])
        
        return True
                
