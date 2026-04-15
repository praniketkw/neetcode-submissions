class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        target = sum(nums)//2
        dp = set()
        dp.add(0)

        for n in nums:
            newdp = dp.copy()
            for subsum in dp:
                if n+subsum==target:
                    return True
                newdp.add(n+subsum)
            dp = newdp
        
        return False
                
                



