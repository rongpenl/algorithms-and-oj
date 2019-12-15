# Definition for singly-linked list.
from heapq import heappush, heappop


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        # filter empty ListNode
        if len(lists) == 0 or all(list(map(lambda x: x == None, lists))):
            return None
        res = None
        if len(lists) == 1:
            return lists[0]
        nodeHeap = []
        for i, node in enumerate(list(filter(lambda x: x != None, lists))):
            heappush(nodeHeap, (node.val, i, node))
        while len(nodeHeap) > 0:
            cur = heappop(nodeHeap)[2]
            if res == None:
                res = cur
                start = res
            else:
                res.next = cur
                res = res.next
            if cur.next != None:
                i += 1
                heappush(nodeHeap, (cur.next.val, i, cur.next))
        # lists has only one element
        return start
