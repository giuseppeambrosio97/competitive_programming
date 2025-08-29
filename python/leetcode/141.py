# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        S = F = head
        while F and F.next:
            S, F = S.next, F.next.next
            if S is F:
                return True
        return False
