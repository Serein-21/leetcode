# Last updated: 1/2/2026, 12:18:11 PM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

        return False
