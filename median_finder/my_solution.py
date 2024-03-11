# https://leetcode.com/problems/find-median-from-data-stream/description/
class MedianFinder:
    '''
    Constraints:
    - -10^5 <= num <= 10^5
    - There will be at least one element in the data structure before calling findMedian.
    - At most 5 * 10^4 calls will be made to addNum and findMedian.

    Steps:
    1. Split up incoming numbers into two lists- small and large. Those that are smaller than the current middle
    element are small, and those that are larger than it are large.
    2. Maintain these lists as heaps so that the root of the small heap is the largest element in it and the root
    of the large heap is the smallest element in it.
    3. If the size of the large heap is greater than the size of the small heap or, if the size of the small heap
    is greater than the size of the large heap + 1, rebalance the heaps.
    4. If the number of elements is even, the median is the mean of the root of the two heaps. Else, it's the root
    of the small heap.

      ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
in:   [ []           , [1]     , [2]     ,  [],           [3],      []]
out:  [ None       ,   None  ,   None    ,  1.5          , None  ,  2.0]
                                             0 1
                                                      2
list: [ [],          , [1],      [1,2]   ,  [1,2]      , [1,2,3] , [1,2,3]   ]
med:  [ None,        ,  1      ,  1.5    ,   1.5       ,   2     ,  2        ]

     0. 1. 2. 3
    [1, 2, 3, 4]
    4
    - when we add a number into the list, the median changes.

    bruteforce: 
    - sort the list every time we add a number.
    - if we have even number of elements in the list:
        - get the half index: half = len(array) // 2
        - return (array[half - 1] + array[half]) / 2 as the median.
    - otherwise, return array[half] as the median.
    

    - sorting the list everytime we add a number is expensive: O(N^2 * logN) in total => avoid sorting every time.

num_added:   1.  ->.  2     ->  3
            [1]  ->  [1, 2] -> [1, 2, 3]
    med:     1   ->   1.5   ->  2


num_added:  1   ->   3     ->  2         ->  2            -> 1               -> 1
list:      [1]. ->  [1,3]  -> [1, 3, 2]. ->  [1, 3, 2, 2] -> [1, 3, 2, 2, 1] -> [1, 3, 2, 2, 1]
sorted:                                                                         [1, 1, 2, 2, 3]
med:        1   ->.  2     ->  2         ->  2            -> 2               -> 2

num_added:  1
list:      [1, 3, 2, 2, 1, 1]
sorted:    [1, 1, 1, 2, 2, 3]
med:        1.5

majority numbers.

=> adding a number that smaller than the current median doesn't change the median.

median: the number that if we sort the list, will be at the middle of the list => the median is greater than 50% numbers on the list and smaller than the other 50% of numbers on the list.

the order of the numbers being added does affect the median
every time we add a number, the length of the list switch from odd -> even or even -> odd => the median can be affected.
    '''
    
    def __init__(self):
        
    # add num to our MedianFinder
    def addNum(self, num: int) -> None:
        
    # returns the median of our datastructure.
    def findMedian(self) -> float: