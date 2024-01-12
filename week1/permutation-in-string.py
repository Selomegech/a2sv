

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        freq_window = defaultdict(int)

        for char in s1:
            freq_s1[char] += 1

        left = 0
        right = 0
        matched = 0

        while right < len(s2):
            if s2[right] in freq_s1:
                freq_window[s2[right]] += 1
                if freq_window[s2[right]] == freq_s1[s2[right]]:
                    matched += 1

            if right - left + 1 >= len(s1):
                if matched == len(freq_s1):
                    return True

                if s2[left] in freq_s1:
                    freq_window[s2[left]] -= 1
                    if freq_window[s2[left]] == freq_s1[s2[left]] - 1:
                        matched -= 1

                left += 1

            right += 1

        return False