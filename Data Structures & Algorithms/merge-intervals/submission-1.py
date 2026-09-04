class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < (len(intervals)):
            currentStart, currentEnd = intervals[i]
            while i + 1 < len(intervals) and currentEnd >= intervals[i + 1][0]:
                i += 1

                currentEnd = max(currentEnd, intervals[i][1])
            res.append([currentStart, currentEnd])
            i += 1
        return res