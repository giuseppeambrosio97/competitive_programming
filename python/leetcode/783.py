# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
from typing import Optional


class Solution:
    # def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    #     """T(n)=O(n)=S(n)."""
        # ll = []

        # def dfs(a: Optional[TreeNode]):
        #     if not a:
        #         return
            
        #     dfs(a.left)
        #     ll.append(a.val)
        #     dfs(a.right)

        # dfs(root)
        
        # min_ = math.inf
        # for i in range(len(ll)-1):
        #     min_ = min(min_, ll[i+1]-ll[i])
        # return min_
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """T(n)=O(n), S(n)=O(1)."""
        self.min_diff = math.inf
        self.prev = None        

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            
            # In-order traversal
            dfs(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)

        dfs(root)
        return self.min_diff
