# Last updated: 1/2/2026, 12:17:25 PM
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Initialize a dictionary to store character counts
        char_count = {}

        # Iterate through the string character by character
        for char in s:
            # Check if the character is already in our count dictionary
            if char in char_count:
                # If it is, this is the first time we've seen it appear twice.
                # Return the character immediately.
                return char
            else:
                # If the character is not in the dictionary,
                # add it with a count of 1, marking its first occurrence.
                char_count[char] = 1

        # According to the problem constraints for "First Letter to Appear Twice",
        # a character is guaranteed to appear twice. This part should ideally
        # not be reached if the input adheres to those constraints.
        # However, as a fallback for general string inputs:
         # Return an empty string or handle the case where no character repeats.