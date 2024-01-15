# https://leetcode.com/problems/task-scheduler/
from collections import defaultdict
from typing import Tuple, List
import functools


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        A: 3
        B: 3
        n   = 2
        ans = 8
        A -> B -> idle -> A -> B -> idle -> A -> B

        edge case: n == 0: return len(tasks)
        A: 2
        B: 3

        A -> B -> _ -> A -> B -> _ -> A 

        max number of time it would take to finish all the tasks in tasks is len(tasks) * (n+1)
        - have an array of length: len(tasks) * (n+1), all initially filled with None (representing "idle"): task_flow
        - have a dictionary called tasks_freq = defaultdict(int)- key: an uppercase letter: str, value: the frequency of that letter in tasks: int. tasks_freq will have up to 26 items.
        - loop thru every character in tasks to populate tasks_freq.
        - have a list called tasks_left = [] to save the pairs of (task, frequency)
        - loop thru tasks_freq to add each pair of (key, value) to tasks_left.
        - sort tasks_left by each task frequency: whichever has the higher frequency will be ranked earlier.
        - have i = 0 to iterate thru tasks_left
        - have a variable called next_avail to save the current smallest index within task_flow where tasks_flow[next_avail] == None.
        - repeat these steps while i < len(tasks_left):
            - get the current task and its frequency: curr_task, freq = tasks_left[i]
            - curr_index = next_avail
            - repeat these steps while freq > 0 and curr_index is smaller than len(task_flow):
                - task_flow[curr_index] = curr_task
                - curr_index is incremented by (n+1)
                - decrement freq by 1.
            - repeat: while task_flow[next_avail] is not None, increment next_avail by 1.
        - i = 0 to iterate thru task_flow
        - count = len(tasks)
        - loop while count is greater than 0 and i < len(task_flow):
            - task_flow[i] is not None, decrement count by 1.
            - increment i by 1.
        - return i
        """
        task_flow = [None for _ in range(len(tasks) * (n+1))]
        task_freq = defaultdict(int)

        for task in tasks:
            task_freq[task] += 1
        tasks_left = []

        for (task, freq) in task_freq.items():
            tasks_left.append((task, freq))

        def compare_by_freq_desc(t1: Tuple[str, int], t2: Tuple[str, int]) -> int:
            return t2[1] - t1[1]
        tasks_left.sort(key=functools.cmp_to_key(compare_by_freq_desc))

        i = 0
        next_avail = 0

        while i < len(tasks_left):
            curr_task, freq = tasks_left[i]
            curr_index = next_avail
            while freq > 0 and curr_index < len(task_flow):
                task_flow[curr_index] = curr_task
                curr_index += (n+1)
                freq -= 1
            while next_avail < len(task_flow) and task_flow[next_avail]:
                next_avail += 1
            i += 1

        i = 0
        count = len(tasks)

        while count > 0 and i < len(task_flow):
            if task_flow[i]:
                count -= 1
            i += 1

        return i
