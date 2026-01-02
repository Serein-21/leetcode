# Last updated: 1/2/2026, 12:18:20 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range (0,n+1) :
            if i not in nums :
                return i 
