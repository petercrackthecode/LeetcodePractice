import copy


class SnapshotArray:
    # Consturctor
    def __init__(self, length):
        self.snapid = 0
        self.node_value = dict()
        self.node_value[0] = dict()
        self.ncount = length

    # Function set_value sets the value at a given index idx to val
    def set_value(self, idx, val):
        if idx < self.ncount:
            self.node_value[self.snapid][idx] = val

    # This function takes no parameters and returns the snapid
    # snapid is the number of times that the snapshot() function was called minus 1
    def snapshot(self):
        self.node_value[self.snapid +
                        1] = copy.deepcopy(self.node_value[self.snapid])
        self.snapid += 1
        return self.snapid - 1

    # Function get_value returns the value at the index idx with the given snapid
    def get_value(self, idx, snapid):
        if snapid < self.snapid and snapid >= 0 and idx < self.ncount:
            return self.node_value[snapid][idx] if idx in self.node_value[snapid] else 0
        else:
            return None

    def __str__(self):
        return str(self.node_value)
