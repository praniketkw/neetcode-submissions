class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        
        sidesum = sum(matchsticks)//4
        sides = [0]*4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i==len(matchsticks):
                return True
            
            for idx in range(4):
                if sides[idx]+matchsticks[i]<=sidesum:
                    sides[idx]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[idx]-=matchsticks[i]
                
                if sides[idx] == 0:
                    break
            return False
        
        return dfs(0)
