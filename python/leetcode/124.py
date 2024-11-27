# Definition for a binary tree node.
from collections import deque
import math
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(array: List[int]) -> Optional["TreeNode"]:
        dd = [TreeNode(val=a) if a else None for a in array]

        for i, t in enumerate(dd):
            if t:
                t.left = dd[2 * i + 1] if 2 * i + 1 < len(dd) else None
                t.right = dd[2 * i + 2] if 2 * i + 2 < len(dd) else None
        return dd[0]


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ = [root.val]
        def dfs(a: Optional[TreeNode]):
            if not a:
                return 0
            maxl = max(0, dfs(a.left))
            maxr = max(0, dfs(a.right))
            max_[0] = max(max_[0], maxl + maxr + a.val)
            return a.val + max(maxl, maxr)
        
        dfs(root)

        return max_[0]


if __name__ == "__main__":
    a = [-1]
    t = Solution().maxPathSum(TreeNode.from_array(a))
    print(t)
