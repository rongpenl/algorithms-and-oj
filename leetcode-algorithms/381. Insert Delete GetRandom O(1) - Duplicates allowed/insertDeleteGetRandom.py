import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.indexes = defaultdict(set)
        # store the index of a value

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.vals.append(val)
        # insert the index of the new val into a set
        self.indexes[val].add(len(self.vals)-1)
        return len(self.indexes[val]) == 1  # if it is new, then it is 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.indexes[val]:
            # if exists, then find one existence of it, replace it with the value of the last element in self.vals.
            replaceD = self.vals[-1]
            valOutIndex = self.indexes[val].pop()  # random one
            self.vals[valOutIndex] = replaceD  # replace
            # update the replaced new index
            self.indexes[replaceD].add(valOutIndex)
            # discard the replaced old index
            self.indexes[replaceD].discard(len(self.vals)-1)
            self.vals.pop()
            return True
        return False
