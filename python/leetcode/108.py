# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(i:int,j:int) -> Optional[TreeNode]:
            if i > j:
                return None
            if i == j:
                return TreeNode(val=nums[i])
            m = i + (j-i) // 2
            node = TreeNode(val=nums[m])
            node.right = build(m+1,j)
            node.left = build(i,m-1)
            return node
        
        return build(0,len(nums)-1)
