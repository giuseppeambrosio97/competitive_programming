# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        lv = self.left.val if self.left is not None else None
        dv = self.right.val if self.right is not None else None
        return f"val: {self.val}, left: {lv}, right: {dv}"

    @staticmethod
    def from_array(nodes) -> "TreeNode":
        trees_dct = {i: TreeNode(val) for i, val in enumerate(nodes)}

        for i in range(len(nodes)):
            if trees_dct[i].val is not None:
                tree = trees_dct[i]
                tree.left = trees_dct[2 * i + 1] if 2 * i + 1 < len(nodes) else None
                tree.right = trees_dct[2 * i + 2] if 2 * i + 2 < len(nodes) else None

        return trees_dct[0]


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            ## find the min
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root

if __name__ == "__main__":
    root = TreeNode.from_array([5, 3, 6, 2, 4, None, 7])
    s = Solution().deleteNode(root, 6)
    print(s)
