# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')  # to store the global maximum path sum

        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Calculate the maximum sum from the left and right subtrees
            left_max = max(helper(node.left), 0)  # only take positive sums
            right_max = max(helper(node.right), 0)  # only take positive sums
            
            # Calculate the price of the current node as the root of the max path
            current_max = node.val + left_max + right_max
            
            # Update the global maximum path sum if the current is greater
            max_sum = max(max_sum, current_max)

            # Return the max sum of the path extending downward
            return node.val + max(left_max, right_max)

        helper(root)
        return max_sum
