class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        ans = 0
        while left < right:
            if skill[left] + skill[right] != skill[0] + skill[-1]:
                return -1
            ans += skill[left] * skill[right]
            left += 1
            right -= 1
        return ans