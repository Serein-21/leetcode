# Last updated: 1/2/2026, 12:18:38 PM
from typing import List
import math # For float('inf')

class Solution:
    def findMin(self, arr: List[int]) -> int:
        if not arr:
            # Or raise an error, or return a specific value
            # depending on problem constraints for an empty array.
            # C++ INT_MAX implies we expect to find something if the array is not empty.
            # If the array can be empty, the behavior needs to be defined.
            # Assuming non-empty as per typical problem statements.
            # If it must handle empty, returning math.inf or raising ValueError might be options.
            return -1 # Placeholder if specific error handling for empty needed

        low = 0
        high = len(arr) - 1
        ans = float('inf') # Equivalent to C++ INT_MAX for initialization

        while low <= high:
            mid = (low + high) // 2

            # This is the crucial logic from your C++ snippet:
            # If the left part (from low to mid) is sorted
            if arr[low] <= arr[mid]:
                # The minimum in this sorted part is arr[low].
                # Update the overall minimum found so far.
                ans = min(ans, arr[low])
                # Move to the right part to see if an even smaller element exists there
                # (this would be the case if the rotation point is in the right part).
                low = mid + 1
            # If the left part is not sorted, it means arr[low] > arr[mid].
            # This implies the rotation (and thus the minimum element) is in this left part,
            # including arr[mid].
            else:
                # arr[mid] is a candidate for the minimum.
                ans = min(ans, arr[mid])
                # The minimum must be in the segment from arr[low] up to arr[mid].
                # So, we search in the left part (including mid initially,
                # but we've already considered arr[mid] for 'ans', so we can shrink high).
                high = mid - 1
        
        return int(ans) if ans != float('inf') else -1 # Or handle as per empty array case