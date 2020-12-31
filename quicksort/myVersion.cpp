#include <iostream>
#include <vector>
#include <algorithm>
#include <exception>
#include <stdexcept>

auto partition(vector<int> &arr, int left, int right) -> void;
auto quickSort(vector<int> &arr) -> void;
auto printArray(const vector<int> &arr) -> void;
auto swap(int &first, int &second) -> void;

int main() {
    // passed case: 0, 8, 1, 2, 7, 9, 3, 4
    // failed case: 5, 2, 3, 1, 9
    vector<int> arr = {0, 8, 1, 2, 7, 9, 3, 4};
    printArray(arr);
    quickSort(arr);
    printArray(arr);
}

auto partition(vector<int> &arr, int left, int right) -> void {
    if (right <= left || right < 0 || left >= arr.size())
        return;
    else if (right - left == 1) {
        if (arr[left] > arr[right]) {
            swap(arr[left], arr[right]);
        }
        return;
    }
    
    int pivot = right,
        start = left,
        end = right - 1;
    
    while (start < end) {
        while (start <= right && arr[start] < arr[pivot])
            ++start;
        while (end >= left && arr[end] > arr[pivot])
            --end;
        if (start < end)
            swap(arr[start], arr[end]);
    }
    
    swap(arr[start], arr[pivot]);
    
    if (start - 1 > left)
        partition(arr, left, start - 1);
    if (start + 1 < right)
        partition(arr, start + 1, right);
}

auto quickSort(vector<int> &arr) -> void {
    partition(arr, 0, arr.size() - 1);
}

auto printArray(const vector<int> &arr) -> void {
    for (auto num : arr) {
        std::cout << num << " ";
    }
    
    std::cout << "\n";
}

auto swap(int &first, int &second) -> void {
    int temp = first;
    first = second;
    second = temp;
}