# Last updated: 1/2/2026, 12:17:35 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maximum = 0

        for ch in s:
            if ch == "(":
                count = count + 1
            maximum = max(maximum, count)

            if ch == ")":
                count = count - 1

        return maximum
