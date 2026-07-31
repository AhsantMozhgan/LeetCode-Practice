# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0  # Initialize count of nodes visited
        self.result = None  # To store the k-th smallest value
        
        def in_order(node):
            if not node:
                return
            
            # Traverse the left subtree
            in_order(node.left)
            
            # Increment the count and check if it's the k-th element
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Traverse the right subtree
            in_order(node.right)

        in_order(root)  # Start in-order traversal
        return self.result
