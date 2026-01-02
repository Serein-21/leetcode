# Last updated: 1/2/2026, 12:18:05 PM
class Solution:
    def frequencySort(self, s: str) -> str:
        # Initialize a dictionary to store character frequencies
        mapit = {}
        # Initialize an empty list to store the parts of the result string
        result_parts = [] # Renamed from 'result' to avoid confusion and indicate it holds parts

        # First pass: Count character frequencies
        for char in s:
            if char in mapit:
                mapit[char] += 1
            else:
                mapit[char] = 1

        # Process characters by frequency until the dictionary is empty
        while mapit:
            # Find the maximum frequency among the remaining characters
            maximum_freq = 0
            # Iterate through the keys currently in mapit to find the max frequency
            # Use list(mapit.keys()) to iterate over a copy of keys to be safe,
            # though just mapit is fine if only reading
            for char in mapit:
                 maximum_freq = max(maximum_freq, mapit[char])

            # Identify characters that have this maximum frequency in this round
            chars_at_max_freq = []
            # Iterate through the keys AGAIN to find which characters have the max frequency
            # Use list(mapit.keys()) to prevent issues if mapit changes (though it won't in this specific loop)
            # or simply iterate over mapit as you were, but don't pop here.
            for char in list(mapit.keys()): # Iterate over a copy of keys
                 if mapit[char] == maximum_freq:
                     chars_at_max_freq.append(char)

            # Process the characters found at maximum frequency
            # Append their repeated strings to result and remove them from mapit
            for char in chars_at_max_freq:
                 # Append the character repeated 'maximum_freq' times
                 result_parts.append(char * maximum_freq)
                 # Remove the character from the frequency map
                 mapit.pop(char) # Now safe to pop as we are not iterating over mapit directly

        # Join the collected string parts into a single result string
        return "".join(result_parts)

# Example Usage:
solution = Solution()
print(f"Input: 'tree', Output: {solution.frequencySort('tree')}")
print(f"Input: 'ccaaatssss', Output: {solution.frequencySort('ccaaatssss')}")
print(f"Input: 'Aabb', Output: {solution.frequencySort('Aabb')}")

