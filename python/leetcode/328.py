# Definition for singly-linked list.

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self):
        return f"val: {self.val}, next val: {self.next.val if self.next else None}"

    @staticmethod
    def from_array(nums: List[int]):
        nodes = [ListNode(num) for num in nums]
        
        for i in range(len(nums)-1):
            nodes[i].next = nodes[i+1]

        return nodes[0]
    
    def pretty_print(self) -> None:
        curr = self
        while curr is not None:
            print(curr)
            curr = curr.next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        root = head
        root_even = head.next
        last_odd = head
        curr_odd = head
        curr_even = head.next
        while curr_odd or curr_even:
            if curr_odd:
                tmp_odd = curr_odd.next.next if curr_odd.next else None
                curr_odd.next = tmp_odd
                curr_odd = tmp_odd
                if curr_odd:
                    last_odd = curr_odd

            if curr_even:
                tmp_even = curr_even.next.next if curr_even.next else None
                curr_even.next = tmp_even
                curr_even = tmp_even

        last_odd.next = root_even


        return root
    
if __name__ == '__main__':
    head = ListNode.from_array([2,1,3,5,6,4,7])

    Solution().oddEvenList(head).pretty_print()


