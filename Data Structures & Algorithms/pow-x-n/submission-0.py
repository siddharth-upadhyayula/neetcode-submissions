class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 0
        def product(x,n):
            nonlocal res
            if x==0:
                return 0.0

            if n==0:
                return 1.0

            if n%2==0:
                multi = product(x,n//2)
                res = multi * multi

            else:
                multi = product(x,(n-1)//2)
                res = multi * multi * x
            
            return res

        if n < 0:
            x = 1 / x
            n = -n
        return product(x,n)