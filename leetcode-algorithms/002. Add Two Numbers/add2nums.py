# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1, L2 = 0, 0
        t1, t2 = l1, l2
        while t1 != None:
            L1 += 1
            t1 = t1.next
        while t2 != None:
            L2 += 1
            t2 = t2.next
        if L1 < L2:
            l1, l2 = l2, l1
        head = l1
        # add l2 to l1
        add = 0
        while l1 != None:
            print(l1.val)
            if l2 != None:
                l1.val += (l2.val+add)
                if l1.val >= 10:
                    add, l1.val = 1, l1.val-10
                else:
                    add = 0
                if l1.next == None:
                    break
                l1, l2 = l1.next, l2.next
            else:
                l1.val += add
                if l1.val >= 10:
                    add, l1.val = 1, l1.val-10
                else:
                    add = 0
                if l1.next == None:
                    break
                l1, l2 = l1.next, None
        if add == 1:
            l1.next = ListNode(1)
        return head
