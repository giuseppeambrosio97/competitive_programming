from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(nums: List[int]) -> "ListNode":
        nodes = [None] * len(nums)
        for i in range(len(nums)):
            node = ListNode(val=nums[i])
            nodes[i] = node
            if i > 0:
                nodes[i-1].next = node
        
        return nodes[0]
    

    def to_list(self) -> list[int]:
        ll = [self.val]
        next = self.next
        while next:
            ll.append(next.val)
            next = next.next
        
        return ll




class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     """Two steps solution"""
    #     curr = head
    #     prev = None
    #     size = 0
    #     while curr:
    #         prev = curr
    #         curr = curr.next
    #         size += 1
    #     if size == n:
    #         return head.next
    #     curr = head
    #     prev = None
    #     cnt = 0
    #     while curr:
    #         prev = curr
    #         curr = curr.next
    #         cnt += 1

    #         if cnt == size - n:
    #             prev.next = curr.next

    #     return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """One step solution"""
        curr, next = None, head
        cnt = 0
        while next and cnt != n:
            curr, next = next, next.next
            cnt += 1

        if curr.next is None:
            return head.next
        
        prev_to_delete, to_delete = None, head


        while curr.next:
            curr = curr.next
            prev_to_delete, to_delete = to_delete, to_delete.next

        
        prev_to_delete.next = to_delete.next

        return head


if __name__ == "__main__":

    s = ListNode.from_list([2,3,4,5])
    head = Solution().removeNthFromEnd(s, 4)
    print(head.to_list())