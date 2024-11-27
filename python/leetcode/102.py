# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return str(self.val)

    @staticmethod
    def from_array(arr: List[int]) -> Optional["TreeNode"]:
        dd = [TreeNode(val=a) if a else None for a in arr]
        for i, d in enumerate(dd):
            if d:
                d.left = dd[2*i + 1] if 2*i < len(dd) else None
                d.right = dd[2*i + 2] if 2*i + 2 < len(dd) else None
        return [] if len(arr) == 0 else dd[0]


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        res = []
        level = []
        while q:
            a, l = q.popleft()
            if len(res) != l:
                res.append(level)
                level = []
            level.append(a.val)
            if a.left:
                q.append((a.left, l + 1))
            if a.right:
                q.append((a.right, l + 1))

        res.append(level)

        return res


if __name__ == "__main__":
    arr = [3, 9, 20, None, None, 15, 7]
    ll = TreeNode.from_array(arr)
    tt = Solution().levelOrder(ll)
    print(tt)
