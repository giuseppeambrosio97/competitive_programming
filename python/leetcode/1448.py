from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def build_from_array(array: List[int]) -> Optional["TreeNode"]:
        trees_dct = {i: TreeNode(val) for i, val in enumerate(array)}

        for i in range(len(array)):
            tree = trees_dct[i]
            tree.left = trees_dct[2*i + 1] if 2*i + 1 < len(array) else None
            tree.right = trees_dct[2*i + 2] if 2*i + 2 < len(array) else None

        return trees_dct[0]

class Output:

    def __init__(self) -> None:
        self.val = 0

    def incr(self):
        self.val += 1

class Solution:

    @staticmethod
    def dfs(a: TreeNode, max_: int, out: Output):
        if a is None or a.val is None:
            return
        max_ = max(max_, a.val)
        if max_ <= a.val:
            out.incr()
        Solution.dfs(a=a.left, max_=max_, out=out)
        Solution.dfs(a=a.right, max_=max_, out=out)

    def goodNodes(self, root: TreeNode) -> int:
        max_ = root.val
        out = Output()
        Solution.dfs(a=root, max_=max_, out=out)
        return out.val

if __name__ == "__main__":
    arr = [3,3,None,4,2]

    root = TreeNode.build_from_array(arr)

    gn = Solution().goodNodes(root=root)
    print(gn)