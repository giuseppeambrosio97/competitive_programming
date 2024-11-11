# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ide(p: Optional[TreeNode], q: Optional[TreeNode]):
            if (p is not None) ^ (q is not None):
                return False
            
            if p is None and q is None:
                return True
            
            if p.val != q.val:
                return False
            
            return ide(p.left, q.left) and ide(p.right, q.right)
        
        return ide(p,q)