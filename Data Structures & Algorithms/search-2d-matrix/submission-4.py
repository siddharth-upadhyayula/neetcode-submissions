class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l=0
        

        m,n = len(matrix), len(matrix[0])
        r=m*n-1

        while l<=r:

            mid = (l+r)//2
            value = matrix[mid//n][mid%n]

            if target==value:
                return True
            elif target<value:
                r=mid-1
            else:
                l=mid+1

        return False


