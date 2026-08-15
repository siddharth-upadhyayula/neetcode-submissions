class Solution:
    import collections
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = collections.deque()
        maxlen = 0
        length = 0

        for i in s:
            if i in res:
                length = len(res)
                res = collections.deque()
                res.append(i)
                maxlen = max(length, maxlen)
            res.append(i)
        return maxlen-1

