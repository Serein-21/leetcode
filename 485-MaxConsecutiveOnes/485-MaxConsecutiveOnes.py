# Last updated: 1/2/2026, 12:18:03 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_no_of_ones = 0
        current_max = 0

        for i in nums:
            if i == 1:
                current_max += 1
                max_no_of_ones = max(max_no_of_ones, current_max)
            else:
                current_max = 0

        return max_no_of_ones
