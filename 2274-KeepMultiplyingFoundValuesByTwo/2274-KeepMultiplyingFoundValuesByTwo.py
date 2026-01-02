# Last updated: 1/2/2026, 12:17:30 PM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # Recursive function
        def recursive(nums, original):
            # Check if original is in the list
            if original in nums:
                # If found, call recursively with original * 2
                return recursive(nums, original * 2)
            else:
                # If not found, return original
                return original
        
        # Call the recursive function and return the result
        return recursive(nums, original)
