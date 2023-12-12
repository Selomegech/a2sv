class Solution:
    def isHappy(self, n: int) -> bool:
        check= set()
        def convert(n):
            n= str(n)
            result=0
            for i in n:
                result += int(i)**2 

            return result 
        while n != 1:
            n=convert(n)
            if n in check:
                return False
            check.add(n)

        return n==1
                