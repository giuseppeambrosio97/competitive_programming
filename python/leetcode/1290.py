from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
        res = 0
        curr = head
        while curr:
            res += curr.val * 2**(cnt-1)
            curr = curr.next
            cnt -= 1
        return res

