from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    @staticmethod
    def _mdbt(a: Optional[TreeNode]) -> int:
        if a is None:
            return 0
        mdbta = max(Solution._mdbt(a.left), Solution._mdbt(a.right)) + 1
        return mdbta

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return Solution._mdbt(root)
    
