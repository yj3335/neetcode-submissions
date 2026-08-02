class Solution:
    def compress(self, chars: List[str]) -> int:
        total = len(chars)
        i = j = 0
        while j < total:
            count = 1
            while j < total - 1 and chars[j] == chars[j+1]:
                count += 1
                j += 1
            
            chars[i] = chars[j]
            i += 1
            if count > 1:
                for val in str(count):
                    chars[i] = val
                    i += 1
            j += 1
        return i