class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        bit = 32

        while bit > 0:
            ans = (ans << 1) | (n & 1)
            n >>= 1
            bit -= 1

        return ans