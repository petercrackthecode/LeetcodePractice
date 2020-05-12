// link: https://leetcode.com/problems/product-of-array-except-self/

vector<int> productExceptSelf(vector<int>& nums) {
    int arraySize= nums.size();
    
    if (arraySize <= 1) {
        throw new std::exception();
    }
    
    std::vector<int> productExceptNumAtIndex(arraySize, 1);
                     
    int index{1};
    
    for (; index < arraySize; ++index) {
        productExceptNumAtIndex[index] *= productExceptNumAtIndex[index - 1] * nums[index - 1];
    }
    for (index = arraySize - 1; index >= 0; --index) {
        if (index != arraySize - 1) {
            savedRight*= nums[index + 1];
        }
        
        productExceptNumAtIndex[index] *= savedRight;
    }

    return productExceptNumAtIndex;
}