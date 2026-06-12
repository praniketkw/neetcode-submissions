class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        cursum = 0
        l = 0

        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                res = min(res, r-l+1)
                cursum-=nums[l]
                l+=1
        
        return res if res!=float("inf") else 0