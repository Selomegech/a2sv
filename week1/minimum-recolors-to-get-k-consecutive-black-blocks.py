class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
        n = len(blocks)
        minRecolors = float('inf')
        
        
        consecutiveBlack = 0
        for i in range(n):
            if blocks[i] == 'B':
                consecutiveBlack += 1
            if i >= k and blocks[i - k] == 'B':
                consecutiveBlack -= 1
            if consecutiveBlack == k:
                return 0
        
        
        for i in range(n):
            recolors = 0
            for j in range(i, n):
                if blocks[j] == 'W':
                    recolors += 1
                if j - i + 1 > k:
                    if blocks[j - k] == 'W':
                        recolors -= 1
                if j - i + 1 >= k:
                    minRecolors = min(minRecolors, recolors)
        
        return minRecolors if minRecolors != float('inf') else 0