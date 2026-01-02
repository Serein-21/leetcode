# Last updated: 1/2/2026, 12:17:46 PM
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer of sliding window
        max_length = 0  # To store the maximum length found
        zero_count = 0  # Number of 0s in current window
        
        # Iterate with the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1  # Count zero as we will consider flipping it

            # If count of zeros exceeds k, move left pointer to shrink window
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1  # Remove the flipped zero from count
                left += 1  # Shrink the window from the left

            # Update maximum length of valid window
            max_length = max(max_length, right - left + 1)

        return max_length
