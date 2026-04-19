class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax, gmin = nums[0], nums[0]
        curmax, curmin = 0,0
        total = 0

        for n in nums:
            curmax = max(n, curmax+n)
            gmax = max(curmax, gmax)
            total+=n
            curmin = min(n, curmin+n)
            gmin = min(curmin, gmin)
        
        return max(gmax, total - gmin) if gmax > 0 else gmax