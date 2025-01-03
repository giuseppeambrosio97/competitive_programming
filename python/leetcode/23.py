from heapq import heapify, heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [(node.val, i, node) for i, node in enumerate(lists) if node is not None]
        heapify(pq)

        dummynode, curr = ListNode()
        while pq:
            nodev, i, node = heappop(pq)

            curr.next = ListNode(nodev)
            curr = curr.next
            node = node.next
            if node:
                heappush(pq, (nodev, i, node))

        return dummynode.next