from typing import Optional, List
from second_implementation import breadth_first_traversal, Node
import unittest


class TestBfs(unittest.TestCase):
    def test_complete_tree(self):
        """
                                 3
                              /    \
                             11     2
                            / \    / \
                          4    5  22  1
                         / \
                        7   8
        """
        seven: Optional["Node"] = Node(7)
        eight: Optional["Node"] = Node(8)
        four: Optional["Node"] = Node(4, seven, eight)
        five: Optional["Node"] = Node(5)
        eleven: Optional["Node"] = Node(11, four, five)
        one: Optional["Node"] = Node(1)
        twenty_two: Optional["Node"] = Node(22)
        two: Optional["Node"] = Node(2, twenty_two, one)
        root_three: Optional["Node"] = Node(3, eleven, two)

        expected: List[int] = [3, 11, 2, 4, 5, 22, 1, 7, 8]
        result: List[int] = breadth_first_traversal(root_three)
        self.assertEqual(expected, result)

    def test_full_tree(self):
        """
                              12
                         /        \
                        37         4
                      /   \       / \
                    21    8      0   6
                                    / \
                                   7   2
                                      /  \
                                     19  -1
        """
        two: Optional["Node"] = Node(2, Node(19), Node(-1))
        six: Optional["Node"] = Node(6, Node(7), two)
        four: Optional["Node"] = Node(4, Node(0), six)
        thirty_seven: Optional["Node"] = Node(37, Node(21), Node(8))
        root_twelve: Optional["Node"] = Node(12, thirty_seven, four)
        expected: List[int] = [12, 37, 4, 21, 8, 0, 6, 7, 2, 19, -1]
        result: List[int] = breadth_first_traversal(root_twelve)
        self.assertEqual(expected, result)

    def test_left_only_tree(self):
        """
               10
             /
            8
           /
          7
         /
        2
        """
        seven: Optional["Node"] = Node(7, Node(2))
        eight: Optional["Node"] = Node(8, seven)
        root_ten: Optional["Node"] = Node(10, eight)
        expected: List[int] = [10, 8, 7, 2]
        result: List[int] = breadth_first_traversal(root_ten)
        self.assertEqual(expected, result)

    def test_right_only_tree(self):
        """
                  37
                    \
                     3
                      \
                      22
                        \
                        10
                          \
                          11
        """
        ten: Optional["Node"] = Node(10, right=Node(11))
        twenty_two: Optional["Node"] = Node(22, right=ten)
        three: Optional["Node"] = Node(3, right=twenty_two)
        root_thirty_seven: Optional["Node"] = Node(37, right=three)
        expected: List[int] = [37, 3, 22, 10, 11]
        result: List[int] = breadth_first_traversal(root_thirty_seven)

        self.assertEqual(expected, result)

    def test_messy_tree(self):
        """
                        10
                      /   \
                     5    -1
                    / \     \
                8(A)  12     8(B)
                  /   /     /
                3    9     -9
                      \
                      100
        """
        nine: Optional["Node"] = Node(9, right=Node(100))
        twelve: Optional["Node"] = Node(12, left=nine)
        eight_A: Optional["Node"] = Node(8, left=Node(3))
        five: Optional["Node"] = Node(5, left=eight_A, right=twelve)
        minus_9: Optional["Node"] = Node(-9)
        eight_B: Optional["Node"] = Node(8, left=minus_9)
        minus_1: Optional["Node"] = Node(-1, right=eight_B)
        ten_root: Optional["Node"] = Node(10, left=five, right=minus_1)

        expected: List[int] = [10, 5, -1, 8, 12, 8, 3, 9, -9, 100]
        result: List[int] = breadth_first_traversal(ten_root)

        self.assertEqual(expected, result)

    def test_empty_tree(self):
        expected: List[int] = []
        result: List[int] = breadth_first_traversal(None)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
