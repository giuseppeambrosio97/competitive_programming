# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        nextv = self.next.val if self.next else None
        return f"val {self.val}, next {nextv}"

    def out(self):
        c = self
        t = []
        while c:
            t.append(c.val)
            c = c.next
        return t

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next



if __name__ == "__main__":

    n1 = ListNode(x=4)
    n2 = ListNode(x=5)
    n3 = ListNode(x=1)
    n4 = ListNode(x=9)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    Solution().deleteNode(n2)

    print(n1.out())
