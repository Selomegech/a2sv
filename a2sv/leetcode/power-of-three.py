class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while True:
            n = n / 3
            if n == 1:
                return True
            if n < 1:
                return False
        