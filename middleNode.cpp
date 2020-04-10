// link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/
ListNode *middleNode(ListNode *head) {
    ListNode *middleNode = head;
    int nodesCounter{0};

    while (middleNode != nullptr)
    {
        ++nodesCounter;
        middleNode = middleNode->next;
    }

    int distanceFromHeadToMiddle = nodesCounter / 2;

    middleNode = head;

    while (distanceFromHeadToMiddle != 0)
    {
        middleNode = middleNode->next;
        --distanceFromHeadToMiddle;
    }
    return middleNode;
}