class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map = {}

        for i in range(len(s)):
            if s[i] in map:
                map[s[i]]+=1
            else:
                map[s[i]]=1

        for j in range(len(t)):
            if t[j] not in map:
                return False
            
            map[t[j]]-=1

            if map[t[j]]<0:
                return False

        return True

        