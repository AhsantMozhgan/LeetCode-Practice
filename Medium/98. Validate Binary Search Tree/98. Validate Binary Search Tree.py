# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lower=float('-inf'), upper=float('+inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            # Check the left subtree with updated upper bound
            if not validate(node.left, lower, val):
                return False
            # Check the right subtree with updated lower bound
            if not validate(node.right, val, upper):
                return False
            
            return True

        return validate(root)
        