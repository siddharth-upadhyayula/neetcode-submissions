class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # 1st iteration racecar, carrace
    # cS[s[0]] = {r:0}->{r:1}
    # cT = {c:0}->{c:1}
    # #2nd 
    # cS[s[1]] = {a:0}->{a:1, r:1}
    # cT = {a:0}->{a:1, c:1}
    # 3rd 
    # cS={r:1, a:1, c:1,}
    # cT={r:1, a:1, c:1}
    # 4th
    # cS=cS={r:1, a:1, c:1, e:1}
        if len(s) != len(t):
            return False
            
        hashS = {}
        hashT = {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        return hashS == hashT

        