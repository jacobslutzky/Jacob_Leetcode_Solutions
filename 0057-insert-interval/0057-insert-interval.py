class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        if not intervals:
            return [newInterval]
        end = len(intervals)-1
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                start = i
                break
            elif newInterval[0] <= intervals[i][1]:
                newInterval[0] = intervals[i][0]
                start = i
                break
            else:
                output.append(intervals[i])
        
        end = len(intervals)
        for i in range(start, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                end=i
                break
            elif newInterval[1] <= intervals[i][1]:
                newInterval[1] = intervals[i][1]
                end=i+1
                break
        
        return output + [newInterval] + intervals[end:]

