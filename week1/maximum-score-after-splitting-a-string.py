class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = 0
        for i in range(1, len(s)):
            leftSubstring = s[:i]
            rightSubstring = s[i:]
            zerosCount = leftSubstring.count('0')
            onesCount = rightSubstring.count('1')
            score = zerosCount + onesCount
            maxScore = max(maxScore, score)
        return maxScore