# Last updated: 1/2/2026, 2:02:28 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3
4        j=len(nums)-1
5        i=0
6
7        emptylist=[]
8
9        while (i<=j):
10            demo=(nums[i]*nums[i]) - (nums[j]*nums[j])
11            if (demo == 0 or demo <0 ):
12                emptylist.insert(0,(nums[j]*nums[j]))
13                j=j-1
14
15            if (demo > 0):
16
17                emptylist.insert(0,(nums[i]*nums[i]))
18                i=i+1
19
20            
21        return emptylist
22
23
24
25            