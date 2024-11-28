# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f"val: {self.val}, next: {self.next}\n"

    @staticmethod
    def from_array(arr: List[int]):
        ll = [ListNode(a) for a in arr]

        for i in range(len(ll)-1):
            ll[i].next = ll[i+1]
        return ll[0]

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        index = k % n
        if index == 0:
            return head
        curr.next = head

        i = 0
        prev, curr = None, head
        while i < n - index:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = None
        return curr


if __name__ == "__main__":
    head = ListNode.from_array([1])
    k = 1
    a = Solution().rotateRight(head, k)
    print(a)
