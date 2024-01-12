class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        right = 0
        maxVowels = 0
        currentVowels = 0

        while right < len(s):
            if s[right] in vowels:
                currentVowels += 1

            if right - left + 1 == k:
                maxVowels = max(maxVowels, currentVowels)
                if s[left] in vowels:
                    currentVowels -= 1
                left += 1

            right += 1

        return maxVowels