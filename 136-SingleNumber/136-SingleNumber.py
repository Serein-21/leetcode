# Last updated: 1/2/2026, 12:18:42 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
         
        sums=0
        sums2=0
        for i in nums :
            sums=sums+i
        
        b=set(nums)

        for i in b :
            sums2=sums2+i
        
        return (2*sums2) - sums