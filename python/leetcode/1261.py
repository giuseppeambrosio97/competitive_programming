# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.M = set()

        def dfs(a: Optional[TreeNode], v: int = 0):
            if a is not None:
                self.M.add(v)
                dfs(a.left, 2*v + 1)
                dfs(a.right, 2*v + 2)
        dfs(root)


    def find(self, target: int) -> bool:
        return target in self.M
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)