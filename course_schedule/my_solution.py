# https://leetcode.com/problems/course-schedule/description/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - Use a dictionary to represent a graph to keep track of the course prerequisites. Call the dictionary num_courses_graph
            - key: current_course.
            - value: courses can only be taken after having finished the current course.
        - [[1, 0], [0, 1], [3, 2]]
        - breadth first traverse through every key in the num_courses_graph see 
        """
        pass
