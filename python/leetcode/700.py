# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(a: Optional[TreeNode], val: int):
    if not a or a.val is None:
        return None
    
    if a.val == val:
        return a
    elif a.val > val:
        return dfs(a.left,val)
    else:
        return dfs(a.right,val)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return dfs(root, val)
    

