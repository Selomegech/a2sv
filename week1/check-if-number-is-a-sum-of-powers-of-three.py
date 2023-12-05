class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0:
            return True
        if n < 0 or n % 3 == 2:
            return False
        return self.checkPowersOfThree(n // 3) or self.checkPowersOfThree(n - 1)