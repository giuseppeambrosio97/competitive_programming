# Definition for a binary tree node.
from typing import List, Literal, Optional

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(array: List[Optional[int]]) -> Optional["TreeNode"]:
        if not array:
            return None
        
        # Create the root of the tree
        root = TreeNode(array[0])
        queue = deque([root])
        
        index = 1  # Start processing the array from the second element
        while index < len(array):
            node = queue.popleft()
            
            # Left child
            if index < len(array) and array[index] is not None:
                node.left = TreeNode(array[index])
                queue.append(node.left)
            index += 1
            
            # Right child
            if index < len(array) and array[index] is not None:
                node.right = TreeNode(array[index])
                queue.append(node.right)
            index += 1
        
        return root

    


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        From each node you can have at most two zigzag path 
        let's say longestZigZag(node)

        basically you can know make a dfs from the root and on each node call the longestZigZag(node) and return the max
        """
        def _longestzigzap(node: Optional[TreeNode], from_: Literal["R", "L"], steps: int):
            if not node:
                return steps
        
            if from_ == "R":
                best = max(
                    steps,
                    _longestzigzap(node=node.left, from_="L", steps=steps+1),
                    _longestzigzap(node=node.right, from_="R", steps=0)
                )
            else:
                best = max(
                    steps,
                    _longestzigzap(node=node.right, from_="R", steps=steps+1),
                    _longestzigzap(node=node.left, from_="L", steps=0)
                )

            return best
        
        return max(_longestzigzap(node=root.right, from_="R", steps=0), _longestzigzap(node=root.left, from_="L", steps=0))


if __name__ == "__main__":
    nodes = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
    root = TreeNode.from_array(nodes)
    s = Solution().longestZigZag(root)
    print(s)