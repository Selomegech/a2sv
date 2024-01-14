
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxScore = 0
        currScore = 0
        
        for i in range(k):
            currScore += cardPoints[i]
        
        maxScore = currScore
        
        for i in range(k-1, -1, -1):
            currScore = currScore - cardPoints[i] + cardPoints[i - k]
            maxScore = max(maxScore, currScore)
        
        return maxScore