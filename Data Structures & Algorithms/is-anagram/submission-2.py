class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for i in s:
            if i in smap:
                smap[i]+=1
            else:
                smap[i]=1
        
        for i in t:
            if i in smap:
                smap[i]-=1 
            else:
                return False
            if smap[i]<0:
                return False
        return True
            