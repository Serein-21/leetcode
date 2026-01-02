# Last updated: 1/2/2026, 12:17:50 PM
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Loop runs until the search space is exhausted
        while left <= right:
            mid = (left + right) // 2  # Use integer division to avoid float index
            
            if nums[mid] == target:
                return mid  # Found the target at index mid
            
            elif target < nums[mid]:
                right = mid - 1  # Target lies in the left half
            
            else:
                left = mid + 1  # Target lies in the right half

        return -1  # Target not found
