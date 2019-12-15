class Solution:
    def countSegments(self, s: str) -> int:
        return sum([e != "" for e in s.split(" ")])
