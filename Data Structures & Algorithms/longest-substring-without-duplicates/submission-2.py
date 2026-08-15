class Solution:
    import collections
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        maxlen = 0
        length = 0

        for i in s:
            if i in res:
                res=[]
            res.append(i)
            length = len(res)
            maxlen = max(length, maxlen)
        return maxlen

