class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        cursum = 0

        for n in nums:
            if cursum<0:
                cursum = 0
            cursum+=n
            res = max(res, cursum)
        
        return res


