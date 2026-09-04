"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        high = 0
        count = 0
        start = [meeting.start for meeting in intervals]
        end = [meeting.end for meeting in intervals]
        start.sort()
        end.sort()
        l = r = 0
        n = len(intervals)
        while True:
            if l >= n and r >= n:
                break        
            elif l >= n:
                count -= 1
                r += 1
            elif r >= n:
                count += 1
                l += 1
            else:
                if end[r] <= start[l]:
                    count -= 1
                    r += 1
                else:
                    count += 1
                    l += 1
            high = max(high, count)
        
        return high