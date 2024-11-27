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

        for i,d in enumerate(dd):
            if d:
                d.left = dd[2*i+1] if 2*i+1 < len(dd) else None
                d.right = dd[2*i+2] if 2*i + 2 < len(dd) else None
        return dd[0] if len(dd) > 0 else None

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)  
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root


if __name__ == "__main__":
    l = Solution().insertIntoBST(TreeNode.from_array([]), 5)
    print(l)