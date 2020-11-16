/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

#include <math.h>

typedef std::vector<Node *> vn; // vn = vector of nodes

class Solution {
public:
    vn breadthFirstSearch(Node *root) {
        std::queue<Node *> nodes;
        nodes.push(root);

        vn answer;

        Node *current = nullptr;

        while (!nodes.empty()) {
            current = nodes.front();
            answer.push_back(current);
            nodes.pop();

            nodes.push(current->left);
            nodes.push(current->right);
        }

        return answer;
    }

    Node *connect(Node *root) {
        if (!root) {
            return root;
        }

        vn linkedlist = breadthFirstSearch(root);

        int nodesCount{0},
            level{1},
            maxNodesAtCurrentLevel{pow(2, level - 1)};

        int linkedListIndex = 0;

        while (linkedListIndex < linkedlist.size()) {
            ++nodesCount;
            if (nodesCount >= maxNodesAtCurrentLevel) {
                ++level;
                maxNodesAtCurrentLevel += pow(2, level - 1);
            } else {
                // the change will be saved because we accessing the value inside the address, aka the reference.
                linkedListIndex != linkedlist.size() - 1 && linkedlist[linkedListIndex]->next = linkedList[linkedListIndex];
            }

            ++linkedListIndex;
        }

        return root;
    }
};