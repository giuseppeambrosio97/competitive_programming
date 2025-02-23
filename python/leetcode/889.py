# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        
        root = TreeNode(preorder[0])
        idx = postorder.index(preorder[1])

        root.left = self.constructFromPrePost(preorder[1:idx+2], postorder[:idx+1])
        root.right = self.constructFromPrePost(preorder[idx+2:], postorder[idx+1:len(postorder)-1])

        return root


if __name__ == "__main__":
    preorder = [1,2,4,5,3,6,7]
    postorder = [4,5,2,6,7,3,1]
    Solution().constructFromPrePost(preorder,postorder)