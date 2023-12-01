# https://leetcode.com/problems/course-schedule/description/
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Graph problem
        output = []
        taken_courses = set()

        form an directed graph using dictionary. Call it graph (key: a course: int, value: a set of depended course: Set[int])
        Initialize the graph: for each sublist [depended, prereq] in prerequisites: add depended to graph[prereq]
        have a dictionary course_degree (key: course: int, value: number of prereq to take: int) to lookup the degree of any course. Loop thru all courses in the graph. for each course's depended, increment course_degree[depended] by 1.
        Use topological sort to find a valid path to traverse thru the graph:
        - have a queue called allowed_courses (deque) to remember all the nodes (courses) with dependent_degree is 0
        - in topological sort, we have to detect cycles. after we pop a node form allowed_courses, if that node already exists in taken_courses, skip it.
        - pop a node from allowed_courses & add it to our output & taken_courses. Decrement the degree of all courses in graph[node] by 1. If the decremented course now has the degree of 0, add it to the queue- allowed_courses.
        - keep doing the steps above while allowed_courses is not empty.

        - if our output's length != len(graph) => we have a cycle that terminates our loop early => return [] (no topological ordering)
        - otherwise, return output
        """
        # edge case: no prerequisites, take courses in any order you want.
        if len(prerequisites) == 0:
            return list(range(numCourses))

        output = deque()
        taken_courses = set()
        graph = defaultdict(set)
        course_degree = defaultdict(int)
        for [depended, prereq] in prerequisites:
            graph[prereq].add(depended)
            course_degree[prereq] = 0 if prereq not in course_degree else course_degree[prereq]
            course_degree[depended] = 1 if depended not in course_degree else (
                course_degree[depended] + 1)

        allowed_courses = deque()
        for course, deg in course_degree.items():
            if deg == 0:
                allowed_courses.append(course)

        # print('course_degree = ', course_degree)

        # no course starts with zero prereq => returns empty array.
        if len(allowed_courses) == 0:
            return []

        while len(allowed_courses) > 0:
            course = allowed_courses.popleft()
            if course in taken_courses:
                # found a cycle
                return []
            output.append(course)
            taken_courses.add(course)
            for depended in graph[course]:
                course_degree[depended] -= 1
                if course_degree[depended] == 0:
                    allowed_courses.append(depended)

        # after the topological sort, all courses must have a degree of zero. If that's not true => we have a cycle.
        for deg in course_degree.values():
            if deg != 0:
                return []
        # if a course isn't listed in prerequisites, it means that course also has no prerequisites & no dependeds
        # add those courses to the beginning of our output
        for i in range(numCourses):
            if i not in taken_courses:
                output.appendleft(i)
                taken_courses.add(i)
        return output
