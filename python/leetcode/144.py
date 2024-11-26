# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive."""
        # ll = []
        # def dfs(a: Optional[TreeNode]):
        #     if not a:
        #         return
        #     ll.append(a.val)
        #     if a.left:
        #         dfs(a.left)
        #     if a.right:
        #         dfs(a.right)  
        # dfs(root)
        # return ll
        """Iterative v1."""
        # if not root:
        #     return []
        # from collections import deque
        # s = deque([root])
        # visited = set([root])
        # ll = []
        # while s:
        #     a = s.pop()
        #     ll.append(a.val)
        #     if a.right and a.right not in visited:
        #         visited.add(a.right)
        #         s.append(a.right)
        #     if a.left and a.left not in visited:
        #         visited.add(a.left)
        #         s.append(a.left)
        # return ll
        """Iterative v2."""
        curr, s = root, []
        res = []

        while curr or s:
            if curr:
                res.append(curr.val)
                s.append(curr.right)
                curr = curr.left
            else:
                curr = s.pop()
        return res
