void merge(std::vector<int> &arr, int l, int m, int r)
{   
    int leftTracer= l,
        rightTracer= m + 1,
        index{0};
        
    std::vector<int> auxiliaryArray(r - l + 1);
    
    while (leftTracer <= m && rightTracer <= r) {
        if (arr[leftTracer] <= arr[rightTracer]) {
            auxiliaryArray[index]= arr[leftTracer];
            ++leftTracer;
        }
        else {
            auxiliaryArray[index]= arr[rightTracer];
            ++rightTracer;
        }
        
        ++index;
    }
    
    if (leftTracer <= m) {
        for (int id= leftTracer; id <= m; ++id) {
            auxiliaryArray[index]= arr[id];
            ++index;
        }
    }
    else {
        for (int id= rightTracer; id <= r; ++id) {
            auxiliaryArray[index]= arr[id];
            ++index;
        }
    }
    
    index= 0;
    
    for (int id= l; id <= r; ++id) {
        arr[id]= auxiliaryArray[index];
        ++index;
    }
     // Your code here
}

void mergeSort(std::vector<int> &arr, int l, int r) {
    if (l < r) {
        int mid= (r - l)/2 + l;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }
}

void mergeSort(std::vector<int> &arr) {
    mergeSort(arr, 0, arr.size() - 1);
}

void printArray(const std::vector<int> &arr) {
    for (auto elem : arr) {
        std::cout << elem << " ";
    }
    
    std::cout << "\n";
}