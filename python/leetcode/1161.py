# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f"Node val: {self.val}, left: {self.left.val if self.left is not None else None}, right: {self.right.val if self.right is not None else None}"

    @staticmethod
    def from_array(nodes) -> "TreeNode":
        trees_dct = {i: TreeNode(val) for i, val in enumerate(nodes) }

        for i in range(len(nodes)):
            if trees_dct[i].val is not None:
                tree = trees_dct[i]
                tree.left = trees_dct[2*i + 1] if 2*i + 1 < len(nodes) else None
                tree.right = trees_dct[2*i + 2] if 2*i + 2 < len(nodes) else None

        return trees_dct[0] 

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        best_level = 1
        best_sum = float("-inf")
        current_level = 1
        while q:
            level_size = len(q)
            sum_ = 0
            for _ in range(level_size):
                node = q.popleft()
                sum_ += node.val

                if node.left is not None and node.left.val is not None:
                    q.append(node.left)
                if node.right is not None and node.right.val is not None:
                    q.append(node.right)

            if sum_ > best_sum:
                best_level = current_level
                best_sum = sum_

            current_level += 1
        return best_level
        

if __name__ == "__main__":
    nodes = [989,None,10250,98693,-89388,None,None,None,-32127]
    root = TreeNode.from_array(nodes)
    print(Solution().maxLevelSum(root))