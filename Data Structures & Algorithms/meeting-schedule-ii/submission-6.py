"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        startPointer, endPointer = 0,0
        maxCount, count = 0, 0
        while startPointer < len(start) and endPointer < len(end):
            if start[startPointer] < end[endPointer]:
                count += 1
                maxCount = max(count, maxCount)
                startPointer += 1
            elif start[startPointer] > end[endPointer]:
                count -= 1
                endPointer += 1
            else:
                startPointer += 1
                endPointer += 1
        return maxCount

        
