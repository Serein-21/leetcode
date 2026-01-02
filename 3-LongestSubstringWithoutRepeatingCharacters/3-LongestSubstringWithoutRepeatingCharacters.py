# Last updated: 1/2/2026, 12:19:00 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Imagine you have a sliding window that moves across the input string.
        We use two pointers, 'l' (left) and 'r' (right), to define this window.
        Our goal is to expand the window ('r' moves forward) as long as we encounter new, unique characters.

        To keep track of the characters within the current window and their last seen positions,
        we use a hash map (dictionary).

        If we encounter a character that is already in our hash map, it means we have a repeating character
        within the current window. To fix this, we need to shrink the window from the left ('l' moves forward)
        until the repeating character is no longer within the window. We also remove the character at the
        left pointer from the hash map as we slide the window.

        At each step, we calculate the current window's length (r - l) and keep track of the maximum length
        we've encountered so far.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.

        Example:
            s = "abcabcbb"
            The longest substring without repeating characters is "abc", with a length of 3.

            s = "bbbbb"
            The longest substring without repeating characters is "b", with a length of 1.

            s = "pwwkew"
            The longest substring without repeating characters is "wke", with a length of 3.
            Note that "pwke" is a subsequence and not a substring.
        """
        l: int = 0  # Initialize the left pointer of the sliding window
        r: int = 0  # Initialize the right pointer of the sliding window
        maxlength: int = 0  # Initialize the variable to store the maximum length found
        hashmap: dict = {}  # Initialize an empty hash map to store characters and their last seen index within the current window

        while r < len(s):  # Continue the loop as long as the right pointer is within the bounds of the string
            if s[r] not in hashmap:  # If the character at the right pointer is not in the hash map (it's a new character in the current window)
                hashmap[s[r]] = r  # Add the character to the hash map and store its current index
                r += 1  # Move the right pointer to expand the window
                maxlength = max(maxlength, r - l)  # Update the maximum length if the current window length is greater
            else:  # If the character at the right pointer is already in the hash map (it's a repeating character)
                del hashmap[s[l]]  # Remove the character at the left pointer from the hash map
                l += 1  # Move the left pointer to shrink the window from the left

        return maxlength  # Return the maximum length of the substring without repeating characters

    
        