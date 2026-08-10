class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        curr_capacity=0
        left = 0
        right = len(heights)-1

        while left<right:
            curr_capacity = min(heights[left], heights[right]) * (right-left)

            if curr_capacity>res:
                res = curr_capacity

            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1

        return res