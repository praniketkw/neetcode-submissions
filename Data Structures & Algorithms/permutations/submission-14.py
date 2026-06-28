class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        count = Counter(nums)

        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if count[nums[i]]!=0:
                    perm.append(nums[i])
                    count[nums[i]]-=1
                    dfs()
                    count[nums[i]]+=1
                    perm.pop()
            
        dfs()
        return res

        
