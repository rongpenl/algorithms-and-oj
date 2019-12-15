# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        start = head
        looper = head
        head = head.next
        while head != None:
            if head.val != looper.val:
                looper.next = head
                looper = looper.next
                head = head.next
                looper.next = None
            else:
                head = head.next
                looper.next = None
        return start
