class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n1, n2 = len(word1), len(word2)
        #w1, w2, flag = 0,0, True
        i, flag = 0, True

        while i < min(n1,n2):
            if flag:
                res += (word1[i])
                flag = False
            else:
                res += (word2[i])
                i += 1
                flag = True
        
        while i < n1:
            res += (word1[i])
            i += 1
        while i < n2:
            res += (word2[i])
            i += 1
        
        return res