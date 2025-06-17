#include <iostream>
#include <vector>

int bin_search(std::vector<int>& a, int target) {
    int left = 0;
    int right = a.size() - 1;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] == target) {
            return mid;
        }

        if (a[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

int main() {
    int n;

    std::cin >> n;

    std::vector<int> arr(n);

    for (size_t i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    const int kToFind = 7;
    int res_index = bin_search(arr, kToFind);
    std::cout << res_index << "\n";
}