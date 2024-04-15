# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.traverse_tree(root, 0)

    def traverse_tree(self, node, total_sum):
        local_sum = total_sum * 10 + node.val
        if node.left is not None:
            local_sum_left = self.traverse_tree(node.left, local_sum)
        else:
            local_sum_left = 0
        if node.right is not None:
            local_sum_right = self.traverse_tree(node.right, local_sum)
        else:
            local_sum_right = 0
            
        if node.left is None and node.right is None:
            return local_sum
            
        return local_sum_left + local_sum_right
                    