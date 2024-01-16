
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0
        max_count = 0
        left = 0
        char_count = defaultdict(int)

        for right in range(n):
            char_count[s[right]] += 1
            max_count = max(max_count, char_count[s[right]])

            if (right - left + 1 - max_count) > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length