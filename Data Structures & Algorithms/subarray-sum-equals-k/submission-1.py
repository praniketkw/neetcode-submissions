class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        premap = {0:1}
        cursum = 0
        res = 0

        for n in nums:
            cursum+=n
            diff = cursum-k
            res+=premap.get(diff,0)
            premap[cursum] = 1+premap.get(cursum,0)
        
        return res