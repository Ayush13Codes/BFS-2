# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # T: O(n), S: O(h)
        if not root:
            return []

        res = []

        def dfs(root, lvl):
            if not root:
                return None
            if lvl == len(res):
                res.append(root.val)

            dfs(root.right, lvl + 1)
            dfs(root.left, lvl + 1)

        dfs(root, 0)
        return res
