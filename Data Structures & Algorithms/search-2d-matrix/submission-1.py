class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = 0
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            if target <= matrix[i][n-1] and target >= matrix[i][0]:
                targetRow = i

        left, right = 0, n-1
        while left<=right:
            mid = left + (right-left)//2
            ele = matrix[targetRow][mid]
            if ele == target:
                return True
            elif ele < target:
                left = mid+1
            else:
                right = mid-1
        return False

        