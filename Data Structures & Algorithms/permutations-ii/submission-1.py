class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        perm = []

        def dfs(i):
            if i>=len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs(i+1)
                    perm.pop()
                    count[n]+=1
        
        dfs(0)
        return res
