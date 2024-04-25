class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        d = {}
        for course, prereq in prerequisites:
            if course in d:
                d[course].append(prereq)
            else:
                d[course] = [prereq]
        for i in range(numCourses):
            if i not in d:
                d[i] = []
        
        visited = set()
        cycle = set()
        output = []
        def dfs(curr_course):
            if curr_course in cycle:
                return False
            if curr_course in visited:
                return True
            cycle.add(curr_course)
            for course in d[curr_course]:
                if not dfs(course):
                    # output.remove(curr_course)
                    # visited.remove(curr_course)
                    return False
            output.append(curr_course)
            visited.add(curr_course)
            cycle.remove(curr_course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return output
        
