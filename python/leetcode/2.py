# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        node = res
        carry = 0
        while l1 or l2:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            v = v1 + v2 + carry
            c, v = divmod(v,10)
            node.next = ListNode(v)
            node = node.next
            carry = c
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if carry:
            node.next = ListNode(carry)
        return res.next