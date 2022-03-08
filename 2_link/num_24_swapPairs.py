# Definition for singly-linked list.

from num_707_MyLinkedList import obj
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        i = 0
        cur = head
        node = ListNode(0)
        node.next = head
        pre = node
        while cur and cur.next:
            nex = cur.next
            nex_nex = cur.next.next
            pre.next = nex
            cur.next = nex_nex
            nex.next = cur
            pre = cur
            cur = nex_nex
        return node.next

s = Solution()
s.swapPairs(obj.head)
