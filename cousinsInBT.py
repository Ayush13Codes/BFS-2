# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # T: O(n), S: O(n)
        if not root:
            return False

        queue = deque([(root, None)])  # (node, parent)

        while queue:
            level_size = len(queue)
            x_parent, y_parent = None, None

            for _ in range(level_size):
                node, parent = queue.popleft()

                # Check if current node matches x or y
                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                # Add children to the queue
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            # If both x and y are found at this level
            if x_parent and y_parent:
                return x_parent != y_parent

            # If one of them is found but not the other, they are not cousins
            if x_parent or y_parent:
                return False

        return False
