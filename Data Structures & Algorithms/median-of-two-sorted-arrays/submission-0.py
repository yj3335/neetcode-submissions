class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #brute
        temp = []
        i,j = 0,0
        m,n = len(nums1), len(nums2)

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        
        while i<m:
            temp.append(nums1[i])
            i += 1
        
        while j<n:
            temp.append(nums2[j])
            j += 1

        if len(temp)%2 != 0:
            return float(temp[len(temp)//2])
        else:
            idx1 = len(temp)//2
            idx2 = idx1 - 1
            s = temp[idx1] + temp[idx2]
            return float((s)/2)