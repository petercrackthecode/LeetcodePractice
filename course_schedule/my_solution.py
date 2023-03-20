# https://leetcode.com/problems/course-schedule/description/
from typing import List, Set, DefaultDict
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = defaultdict(set)
        indegrees_lookup = defaultdict(int)

        for [prereq, offspring_course] in prerequisites:
            course_graph[prereq].add(offspring_course)
            indegrees_lookup[prereq] = 0
            indegrees_lookup[offspring_course] = 0

        def has_cycle(course_graph: DefaultDict[int, Set[int]]):
            topologically_sorted_list = []

            print("indegrees_lookup = ", indegrees_lookup)
            addable_courses = deque()

            # form the indegrees_lookup dictionary
            for _, depended_courses in course_graph.items():
                for course in depended_courses:
                    indegrees_lookup[course] += 1

            print("indegrees_lookup = ", indegrees_lookup)

            # find nodes with zero indegree & add them to addable_courses
            for course, indegree in indegrees_lookup.items():
                if indegree == 0:
                    addable_courses.append(course)

            while len(addable_courses) > 0:
                takeable_course = addable_courses.pop()
                topologically_sorted_list.append(takeable_course)
                for course in course_graph[takeable_course]:
                    indegrees_lookup[course] -= 1
                    if indegrees_lookup[course] == 0:
                        addable_courses.append(course)

            print("topologically_sorted_list = ", topologically_sorted_list)

            return len(topologically_sorted_list) != len(course_graph.keys())

        """
        Return True/False

        We must detect cycles in the graph:
        - If we have cycle: because two courses are interdependent on each other to take,
        we cannot add them -> return False.
        - If we don't have a cycle: return True.

        How do we detect a cycle?
        - From the input, form a graph.
        - Find the cycle within the graph.

        => Use topological sort to detect the cycle within the graph.
        + Forming a graph:
            - Use a dictionary call course_graph:
                - key: the name of the course: str
                - value: a set of courses that are unlocked to take after finishing the current course: Set[str]
        + Have a helper function called have_cycle(course_graph), which returns True if the graph has a cycle, else return False.
        + Return not has_cycle(course_graph)

        + In the have_cycle(course_graph) function, use toplogical sort to order the nodes in the graph based on their number of incoming edges
        (each incoming edge represents a course you must complete before taking the current course):
            - Have an output list call topologically_sorted_list which saves the nodes in the graph in topologically sorted order.
            - Form a dictionary called indegrees_lookup:
                - key: the name of a course: str
                - value: the number of indegrees that the course has (represents the number of prerequisited courses): int.
            - Have a queue (using Python's deque) called addable_courses to keep track of all the courses that we can currently take.
            - Traverse through indegrees_lookup, find the courses with the indegrees of zero (using indegrees_lookup), and
            consecutively add their name to addable_courses.
            - Have a while loop that runs while len(addable_courses) > 0:
                takeable_course = addable_course.pop()
                topologically_sorted_list.append(takeable_course)
                for course in course_graph[takeable_course]:
                    indegrees_lookup[course] -= 1
                    if indgrees_lookup[course] == 0:
                        addable_courses.append(course)
            - Return len(topologically_sorted_list) == len(course_graph.keys()) (if we have a cycle,
            one node will have an indegrees which is greater than other node. Because we never hit the indegree of zero on that node, we
            are stucked in there & never add all the nodes to our topologically_sorted_list).
        """

        print("course_graph = ", course_graph)

        return not has_cycle(course_graph)


num_courses = 1
prerequisites = []

ans = Solution().canFinish(num_courses, prerequisites)

print("ans = ", ans)
