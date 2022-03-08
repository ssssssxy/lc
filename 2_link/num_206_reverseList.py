# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

