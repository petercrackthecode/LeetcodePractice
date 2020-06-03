void postOrderTraversalIteratively(TreeNode *node) {
    std::stack<TreeNode *> nodeStack;
    while (!nodeStack.empty())	{
        while (node) {
            nodeStack.emplace(node->right);
            nodeStack.emplace(node);
            node = node->left;
        }

        node = nodeStack.top();
        nodeStack.pop();
        if (node->right == nodeStack.top())	{
            nodeStack.pop();
            nodeStack.emplace(node);
            node = node->right;
        } 
        else {
            std::cout << node->data << " ";
            node = nullptr;
        }
    }
}