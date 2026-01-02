# Last updated: 1/2/2026, 12:18:36 PM
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # Base case: only one element, it is a peak
        if n == 1:
            return 0
        
        # Check if the first element is a peak
        if nums[0] > nums[1]:
            return 0

        # Check if the last element is a peak
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        # Binary search between the internal elements
        left = 1
        right = n - 2  # Avoid out-of-bounds error

        while left <= right:
            mid = (left + right) // 2

            # Check if mid is a peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # If right neighbor is greater, move right
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Else move left
            else:
                right = mid - 1

        # This return is just a fallback, function will return earlier
        return -1
