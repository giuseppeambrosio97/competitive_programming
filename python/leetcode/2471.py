from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_array(arr: List[int]) -> Optional["TreeNode"]:
        nodes = [TreeNode(val=value) if value is not None else None for value in arr]

        for index, node in enumerate(nodes):
            if node:
                left_child_index = 2 * index + 1
                right_child_index = 2 * index + 2
                node.left = nodes[left_child_index] if left_child_index < len(arr) else None
                node.right = nodes[right_child_index] if right_child_index < len(arr) else None
        
        return nodes[0] if nodes else None

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        total_swaps = 0
        queue = deque([root])

        def count_swaps_to_sort(level_values: List[int]) -> int:
            value_to_index = {value: index for index, value in enumerate(level_values)}
            sorted_values = sorted(level_values)
            swap_count = 0

            for i in range(len(level_values)):
                if level_values[i] != sorted_values[i]:
                    target_index = value_to_index[sorted_values[i]]
                    current_value = level_values[i]

                    # Swap the elements
                    level_values[i], level_values[target_index] = level_values[target_index], level_values[i]

                    # Update the mapping after the swap
                    value_to_index[sorted_values[i]] = i
                    value_to_index[current_value] = target_index

                    swap_count += 1
            
            return swap_count

        while queue:
            current_level_values = [node.val for node in queue]
            total_swaps += count_swaps_to_sort(current_level_values)

            for _ in range(len(queue)):
                current_node = queue.popleft()

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return total_swaps


if __name__ == "__main__":
    root = TreeNode.from_array([1,4,3,7,6,8,5,None,None,None,None,9,None,10])
    t = Solution().minimumOperations(root)
    print(t)
