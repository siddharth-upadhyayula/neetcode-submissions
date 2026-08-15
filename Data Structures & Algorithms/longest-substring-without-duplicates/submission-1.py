class Solution:
    import collections
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        maxlen = 0
        length = 0

        for i in s:
            if i in res:
                length = len(res)
                res = []
                res.append(i)
                maxlen = max(length, maxlen)
            else:
                res.append(i)
        return maxlen

