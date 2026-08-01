# https://leetcode.com/problems/course-schedule/description/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # DFS + Cycle Detection
        # course -> prerequisite courses
        prerequisite_graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            prerequisite_graph[course].append(prerequisite)

        completed_courses = set()
        current_path = set()

        def has_cycle(course):

            # Already completely checked
            if course in completed_courses:
                return False

            # Found a cycle
            if course in current_path:
                return True

            current_path.add(course)

            for prerequisite in prerequisite_graph[course]:
                if has_cycle(prerequisite):
                    return True

            current_path.remove(course)
            completed_courses.add(course)

            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True



# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         # BFS + Topological Sort
#         # prerequisite_graph[course] = courses unlocked after finishing 'course'
#         prerequisite_graph = [[] for _ in range(numCourses)]

#         # Number of prerequisites each course still needs
#         remaining_prerequisites = [0] * numCourses

#         # Build the graph and count prerequisites
#         for course, prerequisite in prerequisites:
#             prerequisite_graph[prerequisite].append(course)
#             remaining_prerequisites[course] += 1

#         # Courses that are ready to be taken
#         available_courses = deque()

#         for course in range(numCourses):
#             if remaining_prerequisites[course] == 0:
#                 available_courses.append(course)

#         completed_courses = 0

#         while available_courses:

#             current_course = available_courses.popleft()
#             completed_courses += 1

#             # Completing the current course satisfies one prerequisite
#             # for every course that depends on it.
#             for next_course in prerequisite_graph[current_course]:

#                 remaining_prerequisites[next_course] -= 1

#                 if remaining_prerequisites[next_course] == 0:
#                     available_courses.append(next_course)

#         return completed_courses == numCourses

        

# DFS + Cycle Detection
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # course -> prerequisite courses
#         prerequisite_graph = defaultdict(list)

#         for course, prerequisite in prerequisites:
#             prerequisite_graph[course].append(prerequisite)

#         completed_courses = set()
#         current_path = set()

#         def has_cycle(course):

#             # Already completely checked
#             if course in completed_courses:
#                 return False

#             # Found a cycle
#             if course in current_path:
#                 return True

#             current_path.add(course)

#             for prerequisite in prerequisite_graph[course]:
#                 if has_cycle(prerequisite):
#                     return True

#             current_path.remove(course)
#             completed_courses.add(course)

#             return False

#         for course in range(numCourses):
#             if has_cycle(course):
#                 return False

#         return True