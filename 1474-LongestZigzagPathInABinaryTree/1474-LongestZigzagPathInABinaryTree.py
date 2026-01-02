# Last updated: 1/2/2026, 12:17:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def f( root , k ,isleft):
            if root :

                if isleft :
                    return max (f(root.left , 1 , True ), f(root.right ,k+1,False ))

                else :
                    return max (f(root.left , k+1,True ),f(root.right ,1,False ))

            return k-1
            
        return (f(root,0,True ))

            

        