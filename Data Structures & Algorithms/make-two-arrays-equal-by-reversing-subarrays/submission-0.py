class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        c1 = Counter(target)
        c2 = Counter(arr)

        if c1==c2:
            return True
        else:
            return False