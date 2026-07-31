# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_side_view = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                current_node = queue.popleft()
                
                # If it's the last node in the level, add it to the right view
                if i == level_length - 1:
                    right_side_view.append(current_node.val)

                # Add left and right children to the queue
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return right_side_view
