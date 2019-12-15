# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        slow, fast = head.next, head.next.next
        if slow == None or fast == None:
            return None
        if head.val == fast.val:
            return head
        while id(slow) != id(fast) and (fast.next != None and fast.next.next != None):
            slow, fast = slow.next, fast.next.next
        if fast.next == None or fast.next.next == None:
            return None
        slow = head
        while id(slow) != id(fast):
            slow, fast = slow.next, fast.next
        return slow
