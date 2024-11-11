# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        0 1 1
        0 1 1
        """
        q = deque([root])
        avgs = []
        
        while q:
            level_sum = 0
            level_count = len(q)

            for _ in range(level_count):
                node = q.popleft()

                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avgs.append(level_sum / level_count)
        return avgs