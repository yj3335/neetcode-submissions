class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        top, bottom = 0, m-1
        while top<=bottom:
            row = top + (bottom-top)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break

        if not (top<=bottom):
            return False
        row = (top+bottom)//2
        left, right = 0, n-1
        while left<=right:
            mid = left + (right-left)//2
            ele = matrix[row][mid]
            if ele == target:
                return True
            elif ele < target:
                left = mid+1
            else:
                right = mid-1
        return False

        