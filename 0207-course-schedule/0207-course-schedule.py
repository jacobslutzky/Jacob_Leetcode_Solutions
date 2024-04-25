class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for course, prereq in prerequisites:
            if course in courses:
                courses[course].append(prereq)
            else:
                courses[course] = [prereq]
        
        cycle = [0]*numCourses
        visited = [0]*numCourses
        def dfs(course):
            if cycle[course]:
                return False
            if visited[course]:
                return True
            cycle[course] = 1
            visited[course]=1
            if course in courses:
                for prereq in courses[course]:
                    if not dfs(prereq):
                        return False
            cycle[course]=0
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


    
