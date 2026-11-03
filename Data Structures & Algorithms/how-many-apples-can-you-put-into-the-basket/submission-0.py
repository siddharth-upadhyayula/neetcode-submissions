class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        count=0
        total=0
        for i in sorted(weight):
            total+=i
            if total>5000:
                return count
            count+=1
        return count