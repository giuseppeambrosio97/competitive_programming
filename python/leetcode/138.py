"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dd = {}
        curr = head
        while curr:
            dd[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            node = dd[curr]
            node.next = dd[curr.next] if curr.next else None
            node.random = dd[curr.random] if curr.random else None
            curr = curr.next
        
        return dd[head]