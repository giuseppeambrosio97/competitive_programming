# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive."""
        # ll = []

        # def dfs(a: Optional[TreeNode]):
        #     if not a:
        #         return []

        #     if a.left:
        #         dfs(a.left)
        #     ll.append(a.val)
        #     if a.right:
        #         dfs(a.right)

        # dfs(root)
        # return ll
        """Iterative v1."""
        # curr, s = root, []
        # visited = set([root])
        # res = []
        # while curr or s:
        #     if curr:
        #         if curr.left is None or curr.left in visited:
        #             visited.add(curr)
        #             res.append(curr.val)
        #             curr = curr.right
        #         else:
        #             s.append(curr)
        #             curr = curr.left
        #     else:
        #         curr = s.pop()
        # return res
        """Iterative v2."""
        curr, s = root, []
        res = []

        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            res.append(curr.val)
            curr = curr.right
        return res
