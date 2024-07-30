# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def __str__(self):
        return f"Node val: {self.val}, left: {self.left.val if self.left is not None else None}, right: {self.right.val if self.right is not None else None}"


    @staticmethod
    def from_array(nodes) -> "TreeNode":
        trees_dct = {i: TreeNode(val) for i, val in enumerate(nodes)}

        for i in range(len(nodes)):
            tree = trees_dct[i]
            tree.left = trees_dct[2*i + 1] if 2*i + 1 < len(nodes) else None
            tree.right = trees_dct[2*i + 2] if 2*i + 2 < len(nodes) else None

        return trees_dct[0]


def dfs(a: TreeNode, target: TreeNode):
    if not a or a.val is None:
        return []

    if a.val == target.val:
        return [a]

    resl = dfs(a.left, target)
    resr = dfs(a.right, target)

    if len(resl) > 0:
        return [a] + resl
    
    if len(resr) > 0:
        return [a] + resr
    
    return []


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root_to_p = dfs(root, p)
        root_to_q = dfs(root, q)

        i = 0

        while i < len(root_to_p) and i < len(root_to_q) and root_to_p[i].val == root_to_q[i].val:
            i += 1


        return root_to_p[max(i - 1,0)]


if __name__ == '__main__':
    nodes = [3,5,1,6,2,0,8,None,None,7,4]
    root = TreeNode.from_array(nodes)
    res = Solution().lowestCommonAncestor(root=root, p=TreeNode(val=7), q=TreeNode(val=4))
    print(res)
