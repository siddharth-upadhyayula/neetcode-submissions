class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sumcalc(n):
            array = []
            total=0
            while n>0:
                array.insert(0, n%10)
                n=n//10

            for i in array:
                total+=i**2

            if total==1:
                return True

            if total in visited:
                return False
            visited.add(total)

            return sumcalc(total)

        return sumcalc(n)