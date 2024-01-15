# https://leetcode.com/problems/task-scheduler/
from typing import List
from collections import defaultdict, deque
from heapq import heappop, heappush


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        n = 2
        tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
        Heap: []
        Queue = []

        Time = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12
        Ch     A -> B -> C -> A -> B -> C -> D -> A -> E ->  B ->  C ->  D

        Since we don't care about the characters, just the minimum number of units our CPU would take (int), we actually don't have to save the characters into our heap and our queue.

        At a time our heap is empty but our queue is not empty (we still have tasks left to do, but they are not ready yet to push back into our heap), that is an idle time, so we are just gonna do nothing else but increment the time by 1.
        """
        time = 0

        ch_freq = defaultdict(int)
        for task in tasks:
            ch_freq[task] += 1
        available_tasks = []
        pending_tasks = deque()

        for ch, freq in ch_freq.items():
            neg_freq = -freq
            heappush(available_tasks, neg_freq)

        # in pending tasks: each task will be saved in the form: (freq, available_time)
        while len(available_tasks) > 0 or len(pending_tasks) > 0:
            time += 1
            if len(pending_tasks) > 0 and pending_tasks[0][1] <= time:
                ready_task = pending_tasks.popleft()
                heappush(available_tasks, ready_task[0])
            if len(available_tasks) == 0:
                # no task is available yet, skip to the next time
                continue
            # available_tasks is not empty
            freq = heappop(available_tasks)
            new_freq = freq + 1
            if new_freq != 0:
                next_avail = time + n + 1
                pending_tasks.append((new_freq, next_avail))

        return time
