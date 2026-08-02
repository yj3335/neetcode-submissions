class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n1, n2 = len(word1), len(word2)
        w1, w2, flag = 0,0, True

        while w1 < n1 and w2 < n2:
            if flag:
                res += (word1[w1])
                w1 += 1
                flag = False
            else:
                res += (word2[w2])
                w2 += 1
                flag = True
        
        while w1 < n1:
            res += (word1[w1])
            w1 += 1
        while w2 < n2:
            res += (word2[w2])
            w2 += 1
        
        return res