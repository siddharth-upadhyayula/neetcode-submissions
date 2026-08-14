class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr=0
        res=0
        sub=""

        for i in range(len(s)):
            while s[i] in sub:
                sub = sub[1:]
            sub+=s[i]
            curr = len(sub)
            res = max(curr, res)
        return res

