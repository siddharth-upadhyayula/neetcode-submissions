class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        res = []


        while left<=right and top<=bottom:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Top to Bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Right to Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Bottom to Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res

            
            