class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0 or n == 0:
            return False
        if n == 1:
            return True
        while True:
            n = n / 4
            if n == 1:
                return True
            if n < 1 :
                return False
            


        