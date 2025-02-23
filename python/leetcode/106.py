# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        h = {}

        for i, a in enumerate(inorder):
            h[a] = i

        def dfs(inorder: List[int], postorder: List[int]):
            if not inorder or not postorder:
                return None
            
            root = TreeNode(postorder[-1])
            mid = h[postorder[-1]]

            root.left = self.buildTree(inorder=inorder[:mid],postorder=postorder[:mid])
            root.right = self.buildTree(inorder=inorder[mid+1:],postorder=postorder[mid:len(postorder)-1])

            return root
        
        
        return dfs(inorder=inorder, postorder=postorder)
        

if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Solution().buildTree(inorder=inorder, postorder=postorder)