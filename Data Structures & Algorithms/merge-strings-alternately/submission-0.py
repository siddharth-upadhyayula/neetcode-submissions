class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1

        res=""

        n = min(len(word1), len(word2))

        for i in range(n):

            res = res + word1[i] + word2[i]


        if len(word1)<len(word2):
            res+=(word2[n:])
        else:
            res+=(word1[n:])

        return res