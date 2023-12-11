class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for week in range(n // 7):
            for day in range(7):
                total += week + day + 1
        for day in range(n % 7):
            total += (n // 7) + day + 1
        return total