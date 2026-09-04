"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        ends = []

        for itv in intervals:
            if ends and itv.start >= ends[0]:
                heapq.heapreplace(ends, itv.end)
            else:
                heapq.heappush(ends, itv.end)

        return len(ends)
