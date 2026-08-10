class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max = 0x7FFFFFFF
        
        while b!=0:
            tmp = (a&b)<<1
            a = (a^b) & mask
            b = tmp & mask
        return a if a <= max else ~(a ^ mask)
         

#         1010  a
#         0110  b
#    a^b  1100
# a&b<<1= 0100 
#           00