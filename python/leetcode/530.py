# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev, self.min_ = None, math.inf

        def dfs(a: Optional[TreeNode]):
            if not a:
                return
            
            dfs(a.left)
            if self.prev is not None:
                self.min_ = min(self.min_, a.val - self.prev)
            self.prev = a.val
            dfs(a.right)

        dfs(root)
        return self.min_