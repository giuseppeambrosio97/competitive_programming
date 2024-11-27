# Definition for a binary tree node.
import math
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

    @staticmethod
    def from_array(arr: List[int]) -> Optional["TreeNode"]:
        dd = [TreeNode(val=a) if a is not None else None for a in arr]

        for i, d in enumerate(dd):
            if d:
                d.left = dd[2 * i + 1] if 2 * i + 1 < len(arr) else None
                d.right = dd[2 * i + 2] if 2 * i + 2 < len(arr) else None
        return dd[0]


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [-math.inf]
        good = [True]

        def dfs(a: Optional[TreeNode]):
            if not a:
                return
            dfs(a.left)
            if prev[0] >= a.val:
                good[0] = False
            prev[0] = a.val
            dfs(a.right)
        dfs(root)
        return good[0]

if __name__ == "__main__":
    arr = [1, 1]
    s = Solution().isValidBST(TreeNode.from_array(arr))
    print(s)
