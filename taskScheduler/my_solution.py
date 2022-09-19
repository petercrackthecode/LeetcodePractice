# https://leetcode.com/problems/task-scheduler/
from collections import deque
from typing import List
import functools


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        1. Have a map which saves the frequencies of tasks called task_frequencies.
        2. Have a deque which saves the task keys (the letters), sorted ascendingly by their frequencies, called 
        available_tasks.
        3. Iterate through the tasks list to populate tasks_frequencies and available_tasks.
        4. Have an array called tasks_queue which illustrates different tasks we would do at the ith time.
        5. Have a variable called tasks_count = len(tasks)
        6. Loop:
           while tasks_count > 0:
        """
        tasks_queue = deque()
        tasks_frequencies = dict()
        tasks_count = len(tasks)

        def compare_ascendingly_by_task_frequencies(task_1, task_2):
            return tasks_frequencies.get(task_1, 0) - tasks_frequencies.get(task_2, 0)

        for task in tasks:
            tasks_frequencies[task] = tasks_frequencies.get(task, 0) + 1
        available_tasks = deque(sorted(tasks_frequencies.keys(), key=functools.cmp_to_key(
            compare_ascendingly_by_task_frequencies)))
        # each section should have n distinctive tasks to pass the condition: there must be at least n units of time
        # between any two same tasks.
        distinctive_tasks_left_in_section = n
        available_tasks_iterator = 0
        while tasks_count > 0:
            if distinctive_tasks_left_in_section <= 0:
                distinctive_tasks_left_in_section = n
                available_tasks_iterator = 0
            if len(available_tasks) <= 0 or available_tasks_iterator >= len(available_tasks):
                tasks_queue.append("idle")
            else:
                curr_task = available_tasks[available_tasks_iterator]
                tasks_queue.append(curr_task)
                tasks_frequencies[curr_task] = tasks_frequencies.get(
                    curr_task, 0) - 1
                tasks_count -= 1
                # since our tasks_queue is sorted ascendingly based on the tasks_frequencies, the first task
                # to run out first will be tasks_frequencies[0]. Hence, we set the iterator back to 0 if the current
                # task runs out
                if tasks_frequencies[curr_task] <= 0:
                    available_tasks.popleft()
                    available_tasks_iterator = 0
            distinctive_tasks_left_in_section -= 1

        return len(tasks_queue)
