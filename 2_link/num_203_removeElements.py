# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        pre = None
        cur = head

        while cur:
            if cur.val == val:
                if not pre:
                    head = cur.next
                    cur = head
                else:
                    pre.next = cur.next
                    cur = pre.next

            else:
                pre = cur
                cur = cur.next

        return head

