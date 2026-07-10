class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax = 1
        curmin = 1

        for n in nums:
            tmp = curmax*n
            curmax = max(curmax*n, curmin*n, n)
            curmin = min(tmp, curmin*n, n)
            res = max(res, curmax)
        
        return res
        

