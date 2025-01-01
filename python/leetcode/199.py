# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def from_array(array: List[int]) -> Optional["TreeNode"]:
        if len(array) == 0:
            return None
        root = TreeNode(array[0])
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if i < len(array) and array[i] is not None:
                node.left = TreeNode(val=array[i])
                q.append(node.left)
            i += 1
            if i < len(array) and array[i] is not None:
                node.right = TreeNode(val=array[i])
                q.append(node.right)
            i += 1
        return root


from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # q = deque([(root, 0)])
        # res = [root.val]
        # running_depth = 0
        # while q:
        #     node, depth = q.popleft()

        #     if depth > running_depth:
        #         running_depth = depth
        #         if len(q) == 0:
        #             res.append(node.val)
        #         else:
        #             res.append(q[-1][0].val)
        #     if node.left:
        #         q.append((node.left, depth+1))
        #     if node.right:
        #         q.append((node.right, depth+1))
        
        # return res
        if not root:
            return []
        q = deque([root])

        s = []

        while q:
            l = []
            for _ in range(len(q)):
                a = q.popleft()
                l.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            
            s.append(l[-1])
        
        return s




if __name__ == '__main__':
    nodes = [1,2]
    root = TreeNode.from_array(array=nodes)

    s = Solution().rightSideView(root)

    print(s)