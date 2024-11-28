# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        s = [root]
        while s:
            a = s.pop()
            if a.right:
                s.append(a.right)
            if a.left:
                s.append(a.left)
            if s:
                a.right = s[-1]
            a.left = None
        return root
