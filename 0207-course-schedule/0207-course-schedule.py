class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for course, prereq in prerequisites:
            if course in courses:
                courses[course].append(prereq)
            else:
                courses[course] = [prereq]
        visited = set()
        curr_visited = set()
        def detect_cycle(course):
            if course in visited:
                return False
            if course in curr_visited:
                return True
            curr_visited.add(course)
            if course in courses:
                for prereq in courses[course]:
                    if detect_cycle(prereq):
                        return True
            curr_visited.remove(course)
            visited.add(course)
            return False
            

        for course in courses:
            if course not in visited:
                if detect_cycle(course):
                    return False
        return True

