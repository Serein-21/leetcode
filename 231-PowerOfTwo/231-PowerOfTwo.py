# Last updated: 1/2/2026, 12:18:24 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if (n==0):
            return False 
        if (n==1):
            return True
        
        elif (n%2 != 0 ):
            return False 

        

        elif (n& (n-1))== 0 :
            return True 

        else :
            return False
        