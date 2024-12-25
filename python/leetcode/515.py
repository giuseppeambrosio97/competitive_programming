# Definition for a binary tree node.
from collections import deque
import math
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            max_ = -math.inf
            for _ in range(len(q)):
                node = q.popleft()
                max_ = max(node.val, max_)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_)
        
        return res

