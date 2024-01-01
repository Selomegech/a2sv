class Solution:
    def maxCoins(self, piles):
        sorted_piles = sorted(piles, reverse=True)  
        n = len(piles) // 3  
        coins = 0
        i = 1  
        
        for _ in range(n):
            coins += sorted_piles[i]  
            i += 2  
        
        return coins