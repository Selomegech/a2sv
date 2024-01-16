class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target_count = n // 4
        char_count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}

        for char in s:
            char_count[char] += 1

        min_length = float('inf')
        left = 0

        for right in range(n):
            char_count[s[right]] -= 1

            while left < n and all(count <= target_count for count in char_count.values()):
                min_length = min(min_length, right - left + 1)
                char_count[s[left]] += 1
                left += 1

        return min_length