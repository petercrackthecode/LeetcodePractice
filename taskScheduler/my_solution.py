# https://leetcode.com/problems/task-scheduler/
import functools
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        tasks = ["A", "A", "B", "A", "C", "C"]
        unique_elements = ["A", "C", "B"]
        tasks_freq = {
            "A": 3,
            "B": 1,
            "C": 2
        }
        tasks_queue = []
        - Have a dictionary called tasks_freq to save the count of tasks in our tasks list.
        - Have a variable called unique_elements which is an array that saves all the tasks’ letters and sorts them based on the tasks_freq of those letters.
        - Have a variable called section_length = n+1.
        - Have a while loop: 
            i = 0
            while tasks_count < len(tasks):
                if section_length == 0:
                    i = 0
                    section_length = n+1
                task_label = unique_elements[i]
                while i < len(unique_elements) and tasks_freq[task_label] <= 0:
                    i += 1
                if i >= len(unique_elements):
                    tasks_queue.add('idle')
                else:
                    tasks_queue.add(task_label)
                    tasks_freq[task_label] = tasks_freq.get(task_label, 0) - 1
                section_length -= 1
                tasks_count += 1
            return len(tasks_queue)

        """
        tasks_freq = dict()
        for task in tasks:
            tasks_freq[task] = tasks_freq.get(task, 0) + 1
        tasks_queue = []

        def compare_task_descendingly(task_1, task_2):
            return tasks_freq.get(task_2, 0) - tasks_freq.get(task_1, 0)

        print('tasks_freq = ', tasks_freq)
        unique_elements = sorted(
            tasks_freq.keys(), key=functools.cmp_to_key(compare_task_descendingly))
        print('unique_elements = ', unique_elements)
        i = 0
        tasks_count = 0
        section_length = n + 1
        while tasks_count < len(tasks):
            print('i = ', i)
            print('section_length = ', section_length)
            if section_length <= 0:
                i = 0
                section_length = n+1

            while i < len(unique_elements) and tasks_freq[unique_elements[i]] <= 0:
                i += 1
            if i >= len(unique_elements):
                # run out of unique tasks to add to the queue, so must append iddle
                # to the section
                tasks_queue.append('idle')
            else:
                tasks_count += 1
                task_label = unique_elements[i]
                tasks_queue.append(task_label)
                tasks_freq[task_label] = tasks_freq.get(task_label, 0) - 1
                # adjust i to move to a new task in our task list.
                i += 1
            section_length -= 1
        print('tasks_queue = ', tasks_queue)
        return len(tasks_queue)
