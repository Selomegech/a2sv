class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        x = self.kthGrammar(n-1 , ceil(k/2))
        if k % 2 == 0:
            x = 1 - x
        return x 
