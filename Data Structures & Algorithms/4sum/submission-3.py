class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quad = []

        def ksum(k, start, target):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i]) 
                    ksum(k-1,i+1,target-nums[i])
                    quad.pop()

            else:
                l,r = start, len(nums)-1
                while l<r:
                    tsum = nums[l]+nums[r]
                    if tsum<target:
                        l+=1
                    elif tsum>target:
                        r-=1
                    else:
                        res.append(quad + [nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1

        ksum(4,0,target)
        return res       