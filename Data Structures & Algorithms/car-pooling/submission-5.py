class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for pas,start,end in trips:
            events.append([start,1,pas])
            events.append([end,0,pas])
        
        events.sort()

        curcap = 0
        for x,typ,numpass in events:
            if typ==1:
                curcap+=numpass
                if curcap>capacity:
                    return False
            else:
                curcap-=numpass
        
        return True


