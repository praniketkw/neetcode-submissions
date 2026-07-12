class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        res = []
        res.append(intervals[0])

        for i in range(1,len(intervals)):
            lastend = res[-1][1]
            if intervals[i][0]>lastend:
                res.append(intervals[i])
            else:
                res[-1][1] = max(lastend, intervals[i][1])
        
        return res


            