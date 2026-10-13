class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        map1 = {}

        for i in range(len(s)):
            if s[i] in map1:
                map1[s[i]]+=1
            else:
                map1[s[i]]=1

        for j in range(len(t)):
            if t[j] in map1:
                map1[t[j]]-=1

            if t[j] not in map1:
                return False
            if map1[t[j]]<0:
                return False

        return True 