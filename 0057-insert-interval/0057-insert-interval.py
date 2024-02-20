class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ## if left_new <= right_old take start of old
        ## if left_new < left_old take start of new
        ## if right_new >= left_old take end of old
        ## if right_new < left_old take end of new
        output = []
        i = 0
        while i < len(intervals):
            if newInterval[0] < intervals[i][0]:
                break
            elif newInterval[0] <= intervals[i][1]:
                newInterval[0] = intervals[i][0]
                break
            else:
                output.append(intervals[i])
                i+=1
        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                break
            elif newInterval[1] <= intervals[i][1]:
                newInterval[1] = intervals[i][1]
                i+=1
                break
            else:
                i+=1
        output.append(newInterval)
        output += intervals[i:]
        return output
            