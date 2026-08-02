class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd = {c : i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j == len(w2): #w2 is prefix of w1, hence not in order
                    return False
                
                if w1[j] != w2[j]: #we found the first different character, check order
                    if orderInd[w2[j]] < orderInd[w1[j]]: # w2 character is lower than w1. not valid
                        return False
                    else: 
                        break #this pair valid, move to next
        # if all valid return true
        return True