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
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self):
        return f"Node val: {self.val}, left: {self.left.val if self.left is not None else None}, right: {self.right.val if self.right is not None else None}"

class Output:

    def __init__(self):
        self.out = False

    def good(self):
        self.out = True

class Solution:

    @staticmethod
    def hps(a: TreeNode, prevSum: int, targetSum: int, out: Output):
        if a is None:
            return
        
        if a.val is not None:
            if (a.val + prevSum == targetSum) and a.left is None and a.right is None:
                out.good()

            if a.left is not None:
                Solution.hps(a.left, prevSum + a.val, targetSum, out)

            if a.right is not None:
                Solution.hps(a.right, prevSum+a.val, targetSum, out)


    def hasPathSumSecond(self, root: Optional[TreeNode], targetSum: int) -> bool:
        out = Output()
        Solution.hps(root, 0, targetSum, out)
        return out.out
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == "__main__":
    arr = [1,2]
    root = TreeNode.build_from_array(arr)

    res = Solution().hasPathSum(root, 3)
    print(res)