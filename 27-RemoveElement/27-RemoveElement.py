# Last updated: 1/2/2026, 12:18:52 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        def removeit(numlist, val):
            # While the value is in the list, keep removing it
            while val in numlist:
                numlist.remove(val)

            # Return the length of the modified list
            return len(numlist)

        # Call the helper function and return the result
        return removeit(nums, val)
