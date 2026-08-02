class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                base = j-i
                ans = max(ans, height*base)
        return ans
