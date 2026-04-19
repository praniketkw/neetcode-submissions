class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for b in bills:
            if b==5:
                five+=1
            if b==10:
                ten+=1
                if five<1:
                    return False
                five-=1
            if b==20:
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False

        return True      
