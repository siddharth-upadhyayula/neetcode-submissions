class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        def countPalindromes(s, l, r):
            nonlocal res
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1

        for i in range(len(s)):
            # odd length
            countPalindromes(s, i, i)

            # even length
            countPalindromes(s, i, i+1)

        return res