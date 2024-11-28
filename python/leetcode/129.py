# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def rsum(a: TreeNode, prefix: str):
            if not a.left and not a.right:
                prefix += str(a.val)
                res[0] += int(prefix)
                return 
            
            if a.left:
                rsum(a.left, prefix+str(a.val))
            if a.right:
                rsum(a.right, prefix+str(a.val))
        
        rsum(root, "")
        return res[0]
        