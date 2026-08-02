class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        element1, count1, element2, count2 = None,0,None,0
        for num in nums:
            if count1 == 0:
                element1 = num
                count1 += 1
            elif num == element1:
                count1 += 1
            elif count2 == 0:
                element2 = num
                count2 += 1
            elif num == element2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for num in nums:
            if element1 == num:
                count1 += 1
            elif element2 == num:
                count2 += 1

        if count1 > (len(nums)//3):
            ans.append(element1)
        if count2 > (len(nums)//3):
            ans.append(element2)
        return ans