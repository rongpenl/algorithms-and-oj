from collections import defaultdict
UNVISITED = 0
VISITING = 1
VISITED = -1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqDict = defaultdict(list)
        for course, prereq in prerequisites:
            preqDict[course].append(prereq)
        # find loops with depth first search
        status = [UNVISITED] * numCourses

        def canTake(course):
            if status[course] in {VISITING, VISITED}:
                return status[course] == VISITED
            status[course] = VISITING
            if any(not canTake(preq) for preq in preqDict[course]):
                return False
            status[course] = VISITED
            return True
        return all(canTake(course) for course in range(numCourses))
