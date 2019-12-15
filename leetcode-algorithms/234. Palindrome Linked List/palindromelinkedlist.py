# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        if len(res) % 2 == 0:
            return res[:len(res)//2] == list(reversed(res[len(res)//2:]))
        else:
            return res[:len(res)//2] == list(reversed(res[len(res)//2+1:]))
