# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        P: parent, L: left, R: right
        PRE: P -> L -> R
        IN: L -> P -> R

        PRE: 
        1) P always the first
        
        Knowing that a node A is a parent node from the preorder traversal by looking at the index of it in the 
        inorder traversal we can say that the remaining nodes at the left of it are the nodes in the left subtree and
        the nodes at the right of it are the nodes in the right subtree.
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # by passing sublist mid in fact count how many nodes are present in the left subtree and based on the fact
        # that in pre-order traversal we visit the left subtree first we have to consider the sublist [1:mid+1] for the
        # the left subtree and for the right subtree we have to take the remaining nodes so [mid+1:]
        root.left = self.buildTree(preorder=preorder[1:mid+1],inorder=inorder[:mid])
        root.right = self.buildTree(preorder=preorder[mid+1:],inorder=inorder[mid+1:])

        return root



if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    Solution().buildTree(preorder, inorder)