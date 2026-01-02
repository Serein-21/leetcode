# Last updated: 1/2/2026, 12:17:23 PM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        minimum=10000000000
        a=set(nums1)
        b=set(nums2)
        for i in  a :
            if i in b:
                minimum=min(minimum,i)
        

        if minimum==10000000000:
            return -1

        else:
            return minimum

        