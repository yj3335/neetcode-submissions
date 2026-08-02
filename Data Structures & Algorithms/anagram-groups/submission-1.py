class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        mp = {}
        for str in strs:
            letters = [0]*26
            for c in str:
                letters[ord(c)-ord('a')] += 1
            tuple_letters = tuple(letters)
            if tuple_letters in mp:
                mp[tuple_letters].append(str)
            else:
                mp[tuple_letters] = [str]
        for key,value in mp.items():
            ans.append(value)
        return ans