# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(arr: List[int]):
        dd = [TreeNode(a) if a is not None else None for a in arr]

        for i,d in enumerate(dd):
            if d:
                d.left = dd[i*2+1] if i*2+1 < len(dd) else None
                d.right = dd[i*2+2] if i*2+2 < len(dd) else None
        return dd[0]


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root

if __name__ == '__main__':
    root = TreeNode.from_array([4,2,7,1,3,6,9])
    a = Solution().invertTree(root)
    print(a)