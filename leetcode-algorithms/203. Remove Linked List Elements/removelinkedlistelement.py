# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, val):
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return head
        cur = head
        while head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return cur
