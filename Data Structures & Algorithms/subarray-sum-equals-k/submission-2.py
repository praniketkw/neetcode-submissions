class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = {0:1}
        cursum = 0
        res = 0

        for n in nums:
            cursum+=n
            res+=presum.get(cursum-k,0)
            presum[cursum] = 1+presum.get(cursum,0)
        
        return res