# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Recursive."""
        # def is_mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        #     if not a and not b:
        #         return True
        #     if not a or not b:
        #         return False
            
        #     return (
        #         a.val == b.val and is_mirror(a.left, b.right) and is_mirror(a.right, b.left)
        #     )
        # if not root:
        #     return True
        # return is_mirror(root.left, root.right)
        """Iterative."""
        if not root:
            return True
        
        s = [(root.left, root.right)]

        while s:
            t1, t2 = s.pop()            
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            s.append((t1.left, t2.right))
            s.append((t1.right, t2.left))
        return True
            
