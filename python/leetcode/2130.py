
from typing import List, Optional
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        n, curr = 0, head

        while curr:
            n += 1
            curr = curr.next


        best, i, limit, curr = -1, 0, (n// 2)-1, head
        pair_sum_i = [0 for _ in range(limit+1)]

        while i < n:
            if i <= limit:
                pair_sum_i[i] += curr.val
            else:
                pair_sum_i[n-i-1] += curr.val
                best = max(best, pair_sum_i[n-i-1])
            i += 1
            curr = curr.next

        return best

        


if __name__ == "__main__":
    ln = ListNode.from_array([1,100000])

    print(Solution().pairSum(ln))