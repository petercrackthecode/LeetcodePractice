# https://leetcode.com/problems/employee-free-time/
import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
            "(" + str(self.start) + ", " + str(self.end) + ")"


def employee_free_time(schedule):
    heap = []
    # Iterate for all employees' schedules
    # and add start of each schedule's first interval along with
    # its index value and a value 0.
    for i in range(len(schedule)):
        heap.append((schedule[i][0].start, i, 0))

    # Create heap from array elements.
    heapq.heapify(heap)

    # Take an empty array to store results.
    result = []

    # Set 'previous' to the start time of first interval in heap.
    previous = schedule[heap[0][1]][heap[0][2]].start

    # Iterate till heap is empty
    while heap:
        # Pop an element from heap and set value of i and j
        _, i, j = heapq.heappop(heap)

        # Select an interval
        interval = schedule[i][j]

        # If selected interval's start value is greater than the
        # previous value, it means that this interval is free.
        # So, add this interval (previous, interval's end value) into result.
        if interval.start > previous:
            result.append(Interval(previous, interval.start))

        # Update the previous as maximum of previous and interval's end value.
        previous = max(previous, interval.end)

        # If there is another interval in current employees' schedule,
        # push that into heap.
        if j + 1 < len(schedule[i]):
            heapq.heappush(heap, (schedule[i][j+1].start, i, j+1))

    # When the heap is empty, return result.
    return result
