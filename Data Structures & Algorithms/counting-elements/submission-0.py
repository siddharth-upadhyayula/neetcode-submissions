class Solution:
    def countElements(self, arr: List[int]) -> int:
        arrset = set(arr)
        count = 0
        for i in arr:
            if i+1 in arrset:
                count+=1
        return count