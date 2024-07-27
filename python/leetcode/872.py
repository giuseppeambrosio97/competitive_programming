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


class Solution:
    @staticmethod
    def lvs(a: Optional[TreeNode]) -> List[int]:
        if a is None:
            return []
        
        if (a.left is None) and (a.right is None) and (a.val is not None):
            return [a.val]

        return Solution.lvs(a.left) + Solution.lvs(a.right) 

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lvs1 = Solution.lvs(root1)
        lvs2 = Solution.lvs(root2)
        return lvs1 == lvs2


if __name__ == "__main__":
    arr = [3,5,1,6,2,9,8,None,None,7,4]

    root = TreeNode.build_from_array(arr)

    lvs = Solution.lvs(root.left.right)
    print(lvs)
