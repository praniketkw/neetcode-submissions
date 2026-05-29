class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        target = sum(nums)//2
        subsum = set()
        subsum.add(0)

        for n in nums:
            sc = subsum.copy()
            for s in subsum:
                if s+n==target:
                    return True
                sc.add(s+n)
            subsum = sc
        
        return False

                



