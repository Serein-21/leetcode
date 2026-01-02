# Last updated: 1/2/2026, 12:17:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    



    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def averageof(List):
            sum=0.00000
            avg=0.00000
            length=len(List)


            for i in List :
                sum = sum + i
        
            avg = (sum/length) * 1.00000

            return avg 

        List =[]
        BigList=[]
        q=deque([ None , root ])

        while True :

            n=q.pop()

            if n :

                

                List.append(n.val)

                if n.left:
                    q.appendleft(n.left)
                
                if n.right:
                    q.appendleft(n.right)

            else :

                avg=averageof(List)

                BigList.append(avg)

                List.clear()

                if q:

                    q.appendleft(None )

                else :
                    break 
        return BigList



