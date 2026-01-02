# Last updated: 1/2/2026, 12:18:13 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        result=[]

        for i in a :
            if i in b:
                result.append(i)

        return result 

        