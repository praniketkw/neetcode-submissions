class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        
        matchsticks.sort(reverse=True)
        sides = [0]*4
        target = sum(matchsticks)//4

        def dfs(i):
            if i>=len(matchsticks):
                return True
            
            for s in range(len(sides)):
                if matchsticks[i]+sides[s]<=target:
                    sides[s]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[s]-=matchsticks[i]
                
                if sides[s]==0:
                    break
            
            return False
        
        return dfs(0)




            

                
