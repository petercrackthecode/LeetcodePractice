# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self) -> None:
        self.cloned_node_lookup_by_val = dict()

    def cloneGraphHelper(self, original: Node, cloned: Node) -> None:
        if not original:
            return

        cloned.val = original.val
        self.cloned_node_lookup_by_val[cloned.val] = cloned

        for neighbor in original.neighbors:
            if neighbor.val in self.cloned_node_lookup_by_val:
                cloned.neighbors.append(
                    self.cloned_node_lookup_by_val[neighbor.val])
                continue

            cloned_neighbor = Node()
            cloned.neighbors.append(cloned_neighbor)
            self.cloneGraphHelper(neighbor, cloned_neighbor)

    def cloneGraph(self, node: Node) -> Node:
        """
        + Iterate through node, set the value of cloned.val = node.val.
        + Have a dictionary call cloned_node_lookup_by_val:
          - key: val.
          - value: the cloned node which we already cloned.
        """
        if not node:
            return None

        ans = Node(node.val)

        self.cloned_node_lookup_by_val[node.val] = ans
        for neighbor in node.neighbors:
            if neighbor.val in self.cloned_node_lookup_by_val:
                ans.neighbors.append(
                    self.cloned_node_lookup_by_val[neighbor.val])
                continue

            cloned_neighbor = Node()
            ans.neighbors.append(cloned_neighbor)
            self.cloneGraphHelper(neighbor, cloned_neighbor)

        return ans
