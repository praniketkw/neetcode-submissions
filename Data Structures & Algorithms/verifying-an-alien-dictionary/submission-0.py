class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderidx = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            
            for j in range(len(w1)):
                if j==len(w2):
                    return False
                if w1[j]!=w2[j]:
                    if orderidx[w1[j]]>orderidx[w2[j]]:
                        return False
                    else:
                        break
        
        return True