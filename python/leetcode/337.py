# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return [0, 0] ## with node, withouth node

            ll = dfs(node.left)
            rr = dfs(node.right)

            return [
                node.val + ll[1] + rr[1],
                max(ll) + max(rr)
            ]  
        return max(dfs(root))

            
