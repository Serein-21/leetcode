# Last updated: 1/2/2026, 12:18:49 PM
class Solution:
    def mySqrt(self, x: int) -> int:

        low=1
        high=x
        ans=0

        while (low<=high):
            mid=(high+low)//2
            
            if(mid*mid == x ):
                return mid
            
            elif(mid*mid > x):
                high=mid-1

            else:
                low=mid+1
                ans = mid 
            
        return ans 
        