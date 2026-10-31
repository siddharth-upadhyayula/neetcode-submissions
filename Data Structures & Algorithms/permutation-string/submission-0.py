class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1arr = list(s1)
        s1arr.sort()
        n = len(s1)
        for i in range(len(s2)):
            if n+i>len(s2):
                return False
            if sorted(s2[i:n+i]) == s1arr:
                return True
        return False