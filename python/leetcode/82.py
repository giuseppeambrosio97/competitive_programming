# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"val: {self.val}, next: {self.next}\n"

    @staticmethod
    def from_array(arr: List[int]):
        nodes = [ListNode(val=a) for a in arr]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def get_head(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None
            if not node.next:
                return node
            
            if node.next.val != node.val:
                return node

            while node and node.next and node.next.val == node.val:
                node = node.next
            return get_head(node.next)

        new_head = get_head(head)
        curr = new_head
        while curr:
            curr.next = get_head(curr.next)
            curr = curr.next

        return new_head


if __name__ == "__main__":
    Solution().deleteDuplicates(ListNode.from_array([-1,-1, 0, 0, 5,1, 1, 1, 2,3, 3,3, 4]))
