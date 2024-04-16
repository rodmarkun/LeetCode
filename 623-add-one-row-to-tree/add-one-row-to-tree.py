# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Depth == 1 case
        if depth == 1:
            new_node = TreeNode(val=val, left=root, right=None)
            # Return new root
            return new_node
        self.traverseTree(root, val, depth, 1)
        return root
    
    def traverseTree(self, node, val, depth, curr_depth):
        # Arrived at destination
        if curr_depth + 1 == depth:
            # Save original trees
            left_tree = node.left
            right_tree = node.right
            # Add new nodes
            node.left = TreeNode(val=val, left=left_tree, right=None)
            node.right = TreeNode(val=val, left=None, right=right_tree)
        # Keep traversing the tree
        else:
            if node.left:
                self.traverseTree(node.left, val, depth, curr_depth + 1)
            if node.right:
                self.traverseTree(node.right, val, depth, curr_depth + 1)
            
        