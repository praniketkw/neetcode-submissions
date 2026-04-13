class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        perm = []

        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    perm.pop()
        
        dfs()
        return res


