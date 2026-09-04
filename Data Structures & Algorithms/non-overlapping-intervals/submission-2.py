class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        i = 1
        minEnd = intervals[0][1]
        count = 0
        while i < len(intervals):
            prevStart, prevEnd = intervals[i - 1]
            currStart, currEnd = intervals[i]
            if currStart < minEnd:
                minEnd = min(minEnd, currEnd)
                count += 1
                i += 1
                continue
            minEnd = currEnd
            i += 1
        return count