# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # if not head:
        #     return -1
        # slow = head
        # fast = head.next
        # while slow != fast:
        #     if not fast or not fast.next:
        #         return -1

        #     fast = fast.next.next
        #     slow = slow.next

        # index1 = head
        # index2 = slow

        # while index1 != index2:
        #     index1 = index1.next
        #     index2 = index2.next
        # return index1

        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast


