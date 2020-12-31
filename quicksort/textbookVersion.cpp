auto partition(vector<int> &arr, int startIndex, int endIndex) -> int;
auto swap(int &a, int &b) -> void;
auto quicksortSublist(vector<int> &arr, int startIndex, int endIndex) -> void;
auto quicksort(vector<int> &arr) -> void;
auto printArray(const vector<int> &arr) -> void;

int main() {
    vector<int> arr = {5, 2, 3, 1, 9};
    printArray(arr);
    quicksort(arr);
    printArray(arr);
}

auto partition(vector<int> &arr, int startIndex, int endIndex) -> int {
    int pivot = arr[endIndex],
        leftIndex = startIndex,
        rightIndex = endIndex - 1;
    
    while (leftIndex <= rightIndex) {
        /* Walk until we find something on the left side that belongs on the right (less than the pivot).
        */
        while (leftIndex <= endIndex && arr[leftIndex] < pivot)
            ++leftIndex;
        /* Walk until we find something on the right side that belongs on the left (greater than or equal to the pivot).
        */
        while (rightIndex >= startIndex && arr[rightIndex] >= pivot)
            --rightIndex;
        
        /* Swap the items at leftIndex and rightIndex, moving the element that's smaller than the pivot to the left half and the element that's larger than the pivot to the right half.
        */
        if (leftIndex < rightIndex) {
            swap(arr[leftIndex], arr[rightIndex]);
        }
        
        /* Unless we've looked at all the elements in the list and are done partitioning. In that case, move the pivot element into its final position.
        */
        else swap(arr[leftIndex], arr[endIndex]);
    }
    
    return leftIndex;
}

auto swap(int &a, int &b) -> void {
    int temp = a;
    a = b;
    b = temp;
}

auto quicksortSublist(vector<int> &arr, int startIndex, int endIndex) -> void {
    // Base case: list with 0 or 1 elements.
    if (startIndex >= endIndex)
        return;
    
    // Divide the array into two smaller subarrays
    int pivotIndex = partition(arr, startIndex, endIndex);
    
    // Recursively sort each subarray
    quicksortSublist(arr, startIndex, pivotIndex - 1);
    quicksortSublist(arr, pivotIndex + 1, endIndex);
}

auto quicksort(vector<int> &arr) -> void {
    quicksortSublist(arr, 0, arr.size() - 1);
}

auto printArray(const vector<int> &arr) -> void {
    for (auto num : arr) {
        std::cout << num << " ";
    }
    
    std::cout << "\n";
}