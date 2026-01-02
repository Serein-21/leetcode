# Last updated: 1/2/2026, 12:17:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        traverse1list = []
        traverse2list = []

        # Helper function to traverse tree1 and collect leaf node values
        def traversetree1(root1, traverse1list):
            if not root1:
                return
            if not root1.left and not root1.right:  # If it's a leaf node
                traverse1list.append(root1.val)     # Append its value
            else:
                traversetree1(root1.left, traverse1list)
                traversetree1(root1.right, traverse1list)

        # Helper function to traverse tree2 and collect leaf node values
        def traversetree2(root2, traverse2list):
            if not root2:
                return
            if not root2.left and not root2.right:  # If it's a leaf node
                traverse2list.append(root2.val)     # Append its value
            else:
                traversetree2(root2.left, traverse2list)
                traversetree2(root2.right, traverse2list)

        # Perform tree traversal and gather leaf sequences
        traversetree1(root1, traverse1list)
        traversetree2(root2, traverse2list)

        # Compare the two lists of leaf values
        return traverse1list == traverse2list
