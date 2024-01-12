class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxLen = 0
        maxCount = 0
        left = 0
        right = 0
        count = {}

        while right < len(answerKey):
            count[answerKey[right]] = count.get(answerKey[right], 0) + 1
            maxCount = max(maxCount, count[answerKey[right]])

            if (right - left + 1) - maxCount > k:
                count[answerKey[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen