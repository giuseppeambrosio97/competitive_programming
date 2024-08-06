from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_array(arr: List[int]):
        nodes = [ListNode(a) for a in arr]

        for i in range(0,len(nodes)-1):
            nodes[i].next = nodes[i+1] 

        return nodes[0]

    def pretty_print(self) -> None:
        curr = self
        while curr is not None:
            print(curr)
            curr = curr.next

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self):
        return f"val: {self.val}, next val: {self.next.val if self.next else None}"
    
    def to_list(self) -> List[int]:
        a, curr = [], self

        while curr:
            a.append(curr.val)
            curr = curr.next

        return a




class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        
        if cnt == 1:
            return None
        
        prev = None
        to_delete = head
        succ = head.next

        median, j = cnt // 2, 0

        while j < median:
            j = j + 1
            prev = to_delete
            to_delete = to_delete.next
            succ = to_delete.next

        prev.next = succ
        return head


if __name__ == "__main__":
    head = ListNode.from_array([1,2])

    print(Solution().deleteMiddle(head).pretty_print())