class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_d = {}
        max_tasks = 0
        num_maxes = 0
        for t in tasks:
            if t in tasks_d:
                tasks_d[t] += 1
            else:
                tasks_d[t] = 1
            if max_tasks == tasks_d[t]:
                num_maxes+=1
            elif max_tasks < tasks_d[t]:
                num_maxes = 1
                max_tasks = tasks_d[t]
               
        situation_1 = max_tasks*(n+1)-n+num_maxes-1
        situation_2 = len(tasks)
        print(max_tasks)
        return max(situation_1,situation_2)
