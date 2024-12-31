# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        s = []
        rl = True

        while q:
            l = [0]*len(q)

            for i in range(len(l)):
                a = q.popleft()
                if rl:
                    l[i] = a.val
                else:
                    l[len(l)-i-1] = a.val

                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)

            s.append(l)
            rl = not rl
        
        return s

