class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            length = str(len(s))
            ans += (length+"#"+s)
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < (len(s)):
            number = 0
            while s[i] != "#":
                number = (number*10) + int(s[i])
                i += 1
            i += 1
            temp = s[i:i+number]
            ans.append(temp)
            i += number

        return ans



