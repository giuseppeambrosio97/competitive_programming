# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.val)

    @staticmethod
    def from_array(arr: List[int]) -> Optional['TreeNode']:
        if not arr:
            return None
        root = TreeNode(arr[0])
        queue = [root]
        i = 1
        while i < len(arr):
            node = queue.pop(0)
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1
        return root

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # q = deque([(root,0)])
        # ll = 0
        # val_level = []
        # while q:
        #     node, level = q.popleft()
        #     if level != ll:
        #         if ll & 1:
        #             for i in range(len(val_level) // 2):
        #                 val_level[i].val, val_level[-i-1].val = val_level[-i-1].val, val_level[i].val
        #         ll = level
        #         val_level = []
            
        #     if node is not None:
        #         val_level.append(node)
        #         q.append((node.left,level+1))
        #         q.append((node.right,level+1))
        # return root
        """More clean way"""
        q = deque([root])
        i = 0

        while q:
            if i & 1:
                for j in range(len(q) // 2):
                    q[j].val, q[-j-1].val = q[-j-1].val, q[j].val

            for _ in range(len(q)):
                a = q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            i += 1
        return root


if __name__ == '__main__':
    arr = [2,3,5,8,13,21,34]
    root = TreeNode.from_array(arr)
    Solution().reverseOddLevels(root)