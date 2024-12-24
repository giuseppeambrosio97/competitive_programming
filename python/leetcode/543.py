# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(arr: List[int]) -> Optional["TreeNode"]:
        dd = [TreeNode(val=a) if a is not None else None for a in arr]

        for i, d in enumerate(dd):
            if d:
                d.left = dd[2 * i + 1] if 2 * i + 1 < len(arr) else None
                d.right = dd[2 * i + 2] if 2 * i + 2 < len(arr) else None
        return dd[0]


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = [-1]

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            l = dfs(node.left)
            r = dfs(node.right)
            ## update diameter
            ## l,r are the heights of the left and right subtree so be have to count the edges to reach those subtree that are two
            ## for leaf nodes this formula will be: -1 -1 + 2 = 0
            max_[0] = max(max_[0],l+r+2)

            return 1 + max(l,r)
        dfs(root)
        return max_[0]
        


if __name__ == "__main__":
    root = TreeNode.from_array([1,2,3,4,5])
    t = Solution().diameterOfBinaryTree(root)
    print(t)
