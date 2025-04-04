# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
from typing import Optional


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dephts = defaultdict(int)
        comp = defaultdict(set)
        id2node = {}
        def dfs(node, depth):
            id2node[node.val] = node
            comp[node.val].add(node.val)
            dephts[node.val] = depth
            if node.left:
                dfs(node.left, depth+1)
                comp[node.val] |= comp[node.left.val]
            if node.right:
                dfs(node.right, depth+1)
                comp[node.val] |= comp[node.right.val]

        dfs(root,0)
        
        ## find the leaf
        
        maxdep = max([v for v in dephts.values()])
        leafs = [k for k,v in dephts.items() if v == maxdep]

        if len(leafs) == 1:
            return id2node[leafs[0]]

        ## the lca will be the node with the highest depht that contains all the leaf nodes
        lca = None
        dep = -1

        for nodeval, nodedep in dephts.items():
            if nodedep > dep and all([leaf in comp[nodeval] for leaf in leafs]):        
                dep = nodedep
                lca = nodeval
        
        
        return id2node[lca]