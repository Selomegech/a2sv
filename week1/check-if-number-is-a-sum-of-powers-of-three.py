class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            if n%3==1:
                n=n//3
            elif n%3==0:
                n=n/3
            else:
                return False
        return True 

            