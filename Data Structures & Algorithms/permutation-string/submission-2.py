class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        count1 = Counter(s1)
        count2 = Counter(s2[:n])

        if count1==count2:
            return True 

        for r in range(n,m):
            count2[s2[r]]+=1
            count2[s2[r-n]]-=1
            if count2[s2[r-n]]==0:
                del count2[s2[r-n]]

            if count2==count1:
                return True

        return False