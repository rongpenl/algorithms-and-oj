# BFS
class Solution:
    def networkDelayTime(self, inputs: List[List[int]], N: int, K: int) -> int:
        times = [dict() for _ in range(N+1)]
        for start, end, time in inputs:
            times[start][end] = time
        resTime = [float("inf") for _ in range(N+1)]
        curLevel = {K}  # only K is visited
        resTime[0], resTime[K] = 0, 0
        while curLevel:
            # print(curLevel,resTime)
            nextLevel = set()
            for start in curLevel:
                for end in times[start]:
                    if resTime[end] > resTime[start] + times[start][end]:
                        resTime[end] = resTime[start] + times[start][end]
                        nextLevel.add(end)
            curLevel = nextLevel
        t = max(resTime)
        return t if t != float("inf") else -1
