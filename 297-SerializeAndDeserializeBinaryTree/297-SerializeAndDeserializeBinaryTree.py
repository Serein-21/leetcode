# Last updated: 1/2/2026, 12:18:17 PM
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        if root:
            # Recursively serialize the tree with node values and nested structures for left and right subtrees
            return str(root.val) + "(" + self.serialize(root.left) + ")(" + self.serialize(root.right) + ")"
        return "X"  # Use "X" to represent null nodes
    
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        if data == "X":  # Base case for null nodes
            return None
        
        # Find the first occurrence of '(' which separates the root value from its subtrees
        data = data.split("(", 1)
        root = TreeNode(int(data[0]))  # Create the root node with the value
        c = 1
        data = data[1]  # Remaining string after the root value
        
        # Find the position where the left subtree ends by balancing parentheses
        for i in range(len(data)):
            if data[i] == "(":
                c += 1
            elif data[i] == ")":
                c -= 1
            if c == 0:  # Left subtree fully processed
                # Deserialize left and right subtrees recursively
                root.left = self.deserialize(data[:i])  # Left subtree string
                root.right = self.deserialize(data[i + 2:-1])  # Right subtree string
                return root

# Example usage:
# codec = Codec()
# tree = codec.deserialize(serialized_data)
# serialized_data = codec.serialize(tree)
