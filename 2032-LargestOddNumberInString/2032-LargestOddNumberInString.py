# Last updated: 1/2/2026, 12:17:31 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Finds the largest-valued odd number that is a non-empty substring of num.

        Args:
            num: A string representing a large integer.

        Returns:
            The largest odd number substring as a string, or "" if none exists.
        """
        n = len(num)
        # Iterate from the rightmost character to the left
        for i in range(n - 1, -1, -1):
            # Check if the character at index i is an odd digit
            if num[i] in '13579':
                # Found the rightmost odd digit.
                # The largest odd substring is the prefix ending at this index.
                return num[0 : i + 1]  # Slice includes index i

        # If the loop completes without finding an odd digit
        return ""

# Example Usage:
sol = Solution()
print(f"'52' -> '{sol.largestOddNumber('52')}'")       # Output: '52' -> '5'
print(f"'4206' -> '{sol.largestOddNumber('4206')}'")     # Output: '4206' -> ''
print(f"'35427' -> '{sol.largestOddNumber('35427')}'")   # Output: '35427' -> '35427'
print(f"'101338' -> '{sol.largestOddNumber('101338')}'") # Output: '101338' -> '10133'