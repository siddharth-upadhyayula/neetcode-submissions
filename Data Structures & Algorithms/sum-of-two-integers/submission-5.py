class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if b > 0 or a <= 0x7FFFFFFF else ~(a ^ mask)