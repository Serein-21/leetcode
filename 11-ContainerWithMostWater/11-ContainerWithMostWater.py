# Last updated: 1/2/2026, 12:18:59 PM
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1

        while l < r:
            hl, hr = height[l], height[r]

            # Calculate the current water area
            curr_water = min(hl, hr) * (r - l)

            # Update max_water if the current area is greater
            if curr_water > max_water:
                max_water = curr_water

            # Move the pointers
            if hl <= hr:
                l += 1
            else:
                r -= 1

        return max_water
