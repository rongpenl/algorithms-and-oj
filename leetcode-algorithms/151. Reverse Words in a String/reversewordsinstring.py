class Solution:
    def reverseWords(self, s):
        res = reversed(list(filter(lambda x: x != "", s.split(" "))))
        return " ".join(res)
