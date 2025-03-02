# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = None

        def inorder(node):
            if not node or self.res is not None:
                return
            inorder(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
            inorder(node.right)
        inorder(root)
        return self.res