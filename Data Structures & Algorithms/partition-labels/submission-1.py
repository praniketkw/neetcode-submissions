class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastidx = {}

        for i,c in enumerate(s):
            lastidx[c]=i
        
        res = []
        size = 0
        end = 0

        for i,c in enumerate(s):
            end = max(end, lastidx[c])
            size+=1
            if i==end:
                res.append(size)
                size = 0

        return res
