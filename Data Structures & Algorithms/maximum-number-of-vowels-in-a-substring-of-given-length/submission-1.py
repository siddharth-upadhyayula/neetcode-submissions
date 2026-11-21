class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        sub=""
        count=0
        current=0
        l=0
        for i in range(len(s)):
            sub+=s[i]
            if s[i] in vowels:
                current+=1
            if len(sub)==k:
                count = max(count, current)
                if sub[0] in vowels:
                    current -= 1
                sub=sub[1:]
                

        return count