from typing import Optional, List
import collections as cll
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
        self.out = 0

    def incr(self, val: int = 1):
        self.out += val

class Solution:

    @staticmethod
    def ps(a: TreeNode, prevSum: int, target: int, output: Output):
        if a.val is not None:
            if prevSum + a.val == target:
                output.incr()
        
            if a.left is not None:
                Solution.ps(a.left, prevSum + a.val, target, output)

            if a.right is not None:
                Solution.ps(a.right, prevSum + a.val, target, output)

    @staticmethod
    def dfs(a: TreeNode, targetSum: int, output: Output):
        if a is None:
            return
        
        Solution.ps(a, 0, targetSum, output)
        
        if a.left is not None:
            Solution.dfs(a.left, targetSum, output)

        if a.right is not None:
            Solution.dfs(a.right, targetSum, output)

    def pathSumWorst(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        non-balanced tree
        T(n) = T(n-1) + n
             = O(n^2)
        balanced tree
        T(n) = 2T(n/2) + n
             = O(nlogn)
        S(n) = O(1)
        where n is the cost of Solution.ps
        """
        output = Output()
        Solution.dfs(root, targetSum, output)
        return output.out
    

    @staticmethod
    def dfs2(a: TreeNode, targetSum: int, sumCounts: cll.defaultdict, currentSum: int, output: Output):
        if not a or a.val is None:
            return
        
        currentSum += a.val

        output.incr(sumCounts[currentSum - targetSum])

        sumCounts[currentSum] += 1

        Solution.dfs2(a.left, targetSum, sumCounts, currentSum, output)
        Solution.dfs2(a.right, targetSum, sumCounts, currentSum, output)

        sumCounts[currentSum] -= 1
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        sumCounts = cll.defaultdict(int)

        sumCounts[0] = 1

        out = Output()

        Solution.dfs2(root, targetSum, sumCounts, 0, out)

        return out.out




if __name__ == "__main__":
    arr = [10,5,-3,3,2,None,11,3,-2,None,1]

    root = TreeNode.build_from_array(arr)

    res = Solution().pathSum(root, 8)
    print(res)