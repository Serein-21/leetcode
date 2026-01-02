# Last updated: 1/2/2026, 12:18:18 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num={}

        for i in nums:
            if i  in num:
                return i

            else:
                num[i]=1
