class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        count2 = {}
        for i in range(n):
            count2[s2[i]] = 1 + count2.get(s2[i], 0)

        left = 0
        for right in range(n, m):
            if count1 == count2:
                return True
            count2[s2[right]] = 1 + count2.get(s2[right], 0)
            count2[s2[left]] -= 1
            if count2[s2[left]] == 0:
                count2.pop(s2[left])
            left += 1
        return count1==count2
