# https://leetcode.com/problems/snapshot-array/
from typing import List, Tuple


class SnapshotArray:

    def __init__(self, length: int):
        """
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
        if index < 0 or index >= len(self.arr) or snap_id < 0:
            return -1

        def find_val_at_snap_id(vals_at_index: List[Tuple[int, int]]) -> int:
            nonlocal index, snap_id

            left, right = 0, len(vals_at_index) - 1

            while left <= right:
                mid = left + (right-left) // 2
                curr_snap_id, val = vals_at_index[mid]
                # last element bound
                if mid == len(vals_at_index) - 1 and curr_snap_id <= snap_id:
                    return mid
                # first element bound
                elif mid == 0 and curr_snap_id >= snap_id:
                    return mid
                elif curr_snap_id <= snap_id < vals_at_index[mid+1][0]:
                    return mid
                elif curr_snap_id > snap_id:
                    # move left
                    right = mid - 1
                else:  # move right
                    left = mid + 1

            return 0

        # List[Tuple[int, int]]
        vals_at_index = self.arr[index]
        found_index = find_val_at_snap_id(vals_at_index)
        return vals_at_index[found_index][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
