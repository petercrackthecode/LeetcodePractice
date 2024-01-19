# https://leetcode.com/problems/snapshot-array/
from typing import List, Tuple


class SnapshotArray:

    def __init__(self, length: int):
        """
        data structures:
        - a list of int: arr
        - a snap id: int
        - a dictionary:
            - key: snap_id: int
            - value: arr at time snap_id

        - Create a new entry in the dictionary by copying the previous value at snapid to snapid + 1.
        - Increment the value of snapid by 1 to keep track of the number of snapshots taken.
        - Return the index of the snapshot taken recently, which is the index at snapid - 1.

        """
        self.arr: List[List[Tuple[int, int]]] = [
            [(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # 0: [(0, 1), (4, 2), (5, 3)]
        if index < 0 or index > len(self.arr) - 1:
            return
        if len(self.arr[index]) == 0:
            self.arr[index].append((self.snap_id, val))
        else:
            last_snap_id = self.arr[index][-1][0]
            if self.snap_id == last_snap_id:
                self.arr[index][-1] = (last_snap_id, val)
            else:
                # new val created at a new time
                self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index < 0 or index >= len(self.arr):
            return -1

        # List[Tuple[int, int]]
        values_thru_snap_id = self.arr[index]
        # curr_index
        curr_index = len(values_thru_snap_id) - 1

        while curr_index >= 0 and values_thru_snap_id[curr_index][0] > snap_id:
            curr_index -= 1
        if curr_index < 0:
            return -1
        return values_thru_snap_id[curr_index][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
