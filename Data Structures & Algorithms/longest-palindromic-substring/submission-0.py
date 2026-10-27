class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        def findlongestPalindrome(s, l, r):
            nonlocal res

            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1

            curr = s[l+1:r]
            if len(curr)>len(res):
                res = curr

        for i in range(len(s)):

            findlongestPalindrome(s,i,i)

            findlongestPalindrome(s,i,i+1)

        return res