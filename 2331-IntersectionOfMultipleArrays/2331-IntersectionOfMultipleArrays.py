# Last updated: 1/2/2026, 12:17:29 PM
from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Start with the first list as reference
        demoset = nums[0]

        # Loop through the rest of the lists
        for i in range(1, len(nums)):
            anotherset = []  # Reset for each iteration

            for element in demoset:
                if element in nums[i]:  # Check if element exists in current list
                    anotherset.append(element)

            demoset = anotherset  # Update the common elements

            # Early exit if no common elements
            if not demoset:
                return []

        return sorted(demoset)
