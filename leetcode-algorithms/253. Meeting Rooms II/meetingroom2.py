import heapq
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        min_heap = [intervals[0].end] # stores only end_time
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start < min_heap[0]:
                heapq.heappush(min_heap, interval.end)
            else:
                heapq.heappushpop(min_heap, interval.end)
        return len(min_heap)