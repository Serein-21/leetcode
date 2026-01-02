# Last updated: 1/2/2026, 12:18:28 PM

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Find the minimal length of a contiguous subarray of which the sum 
        is at least the given target.

        Uses a sliding window approach to maintain the smallest valid 
        subarray found while traversing the array.

        Args:
            target (int): The minimum sum required.
            nums (List[int]): List of positive integers.

        Returns:
            int: Length of the smallest subarray with sum ≥ target.
                 Returns 0 if no such subarray exists.

        Raises:
            ValueError: If `nums` is empty or contains non-positive integers.

        Notes:
            - The sliding window approach ensures O(n) time complexity.
            - Only works correctly for positive integers.
        """

        # Block: Initialize tracking variables
        min_length = float('inf')  # Initialize with infinity to track minimum window size
        summ = 0                   # Cumulative sum of current window
        l = 0                      # Left pointer of the sliding window

        # Block: Expand the right end of the window
        for r in range(len(nums)):
            summ += nums[r]  # Add current value to running sum

            # Block: Shrink the window from the left as long as sum ≥ target
            while summ >= target:
                # Line: Update minimum length if current window is smaller
                min_length = min(min_length, r - l + 1)

                # Line: Remove leftmost element and move left pointer right
                summ -= nums[l]
                l += 1

        # Block: Return result — either found length or 0 if not found
        return min_length if min_length < float('inf') else 0
