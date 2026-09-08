class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            digits = len(str(i))
            total += (digits - 1) // 3
        return total
        