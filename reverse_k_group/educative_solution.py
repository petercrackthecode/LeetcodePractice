from typing import Optional, Tuple


class Node:
    def __init__(self, data: int, next: Optional["Node"] = None):
        self.data = data
        self.next = next


def reverse_linked_list(head: Optional["Node"], k: int) -> Tuple[Optional["Node"]]:
    prev, curr, next = None, head, None
    for _ in range(k):
        # temporarily store the next node
        next: Optional["Node"] = curr.next
        # reverse the curr node
        curr.next = prev
        # before we move to the next node, point prev to the curr node
        prev = curr
        # move to the next node
        curr = next
    return prev, curr


def reverse_k_groups(head: Optional["Node"], k: int):
    dummy = Node(0, head)
    # dummy always points to the node before the head of the linked list
    ptr: Optional["Node"] = dummy

    while ptr:
        tracker = ptr
        for _ in range(k):
            if not tracker:
                break

            tracker = tracker.next
        if not tracker:
            break

        prev, curr = reverse_linked_list(ptr.next, k)
        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = curr
        ptr.next = prev
        ptr = last_node_of_reversed_group

    return dummy.next
