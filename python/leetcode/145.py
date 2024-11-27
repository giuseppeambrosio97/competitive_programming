# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(arr: List[int]) -> Optional["TreeNode"]:
        dd = [TreeNode(val=a) if a else None for a in arr]

        for i,d in enumerate(dd):
            if d:
                d.left = dd[2*i+1] if 2*i + 1 < len(dd) else None
                d.right = dd[2*i+2] if 2*i+2 < len(dd) else None
        
        return dd[0] if len(dd) > 0 else None

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive"""
        # ll = []

        # def dfs(a: Optional[TreeNode]):
        #     if not a:
        #         return
        #     if a.left is not None:
        #         dfs(a.left)
        #     if a.right is not None:
        #         dfs(a.right)
        #     ll.append(a.val)

        # dfs(root)

        # return ll
        """Iterative"""
        if root is None:
            return []
        stack = deque([root])
        visited = set()
        ll = []

        while stack:
            a = stack.pop()
            if a:
                if a not in visited:
                    stack.append(a)
                    stack.append(a.right)
                    stack.append(a.left)
                else:
                    ll.append(a.val)
                visited.add(a)
        return ll
    
if __name__ == "__main__":
    arr = [5,1,4,None,None,2,3]
    a = Solution().postorderTraversal(TreeNode.from_array(arr))
    print(a)