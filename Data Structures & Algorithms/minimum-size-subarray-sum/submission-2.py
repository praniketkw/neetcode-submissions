class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        l = 0
        cursum = 0

        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                res = min(res, r-l+1)
                cursum-=nums[l]
                l+=1
        
        return res if res!=len(nums)+1 else 0