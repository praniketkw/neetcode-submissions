class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for p,s,d in trips:
            events.append([s,1,p])
            events.append([d,0,p])
        
        events.sort(key = lambda x:(x[0],x[1]))

        curcap = 0

        for pos,typ,pas in events:
            if typ==1:
                curcap+=pas
                if curcap>capacity:
                    return False
            else:
                curcap-=pas
        
        return True

