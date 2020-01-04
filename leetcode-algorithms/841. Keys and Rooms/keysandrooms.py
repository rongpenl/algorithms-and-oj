class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = set()
        N = len(rooms)
        opened.add(0)
        toOpen = rooms[0]
        while toOpen:
            nextRound = set()
            for room in toOpen:
                for newKey in rooms[room]:
                    if newKey not in opened:
                        nextRound.add(newKey)
                opened.add(room)
            toOpen = list(nextRound)
        if len(opened) == N:
            return True
        return False
