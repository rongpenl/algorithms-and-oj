"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        # write your code here
        ret = [None for _ in range(len(hashTable)*2)]
        capacity = len(ret)
        for node in hashTable:
            while node != None:
                newKey = node.val % capacity
                if ret[newKey] == None:
                    ret[newKey] = ListNode(node.val)
                else:
                    existedEle = ret[newKey]
                    while existedEle.next != None:
                        existedEle = existedEle.next
                    existedEle.next = ListNode(node.val)
                node = node.next
        return ret
