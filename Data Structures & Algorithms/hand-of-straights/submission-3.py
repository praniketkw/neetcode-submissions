class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        count = Counter(hand)
        minheap = []

        for n,c in count.items():
            heapq.heappush(minheap, n)
        
        while minheap:
            minimum = minheap[0]

            for i in range(minimum, minimum+groupSize):
                if i not in count or count[i]==0:
                    return False
                count[i]-=1
            while minheap and count[minheap[0]]==0:
                heapq.heappop(minheap)
        
        return True


