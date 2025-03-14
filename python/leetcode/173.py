# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class BSTIterator:

    """O(n)=S(n), operation run in O(1)=T(n)"""
    # def __init__(self, root: Optional[TreeNode]):
    #     self.nodes = []
        
    #     def inorder(node: Optional[TreeNode]):
    #         if not node:
    #             return
    #         inorder(node.left)
    #         self.nodes.append(node.val)
    #         inorder(node.right)
        
    #     inorder(root)
    #     self.idx = 0

    # def next(self) -> int:
    #     self.idx += 1
    #     return self.nodes[self.idx-1]

    # def hasNext(self) -> bool:
    #     return self.idx < len(self.nodes)
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()

        curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.right
        return res.val  
    
    def hasNext(self) -> bool:
        return len(self.stack) != 0
        