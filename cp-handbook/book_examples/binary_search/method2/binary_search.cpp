#include <cstddef>
#include <iostream>
#include <vector>

int bin_search(std::vector<int>& a, int target) {
    int n = a.size();
    int start = 0;
    for (size_t step = n / 2; step >= 1; step /= 2) {
        while (start + step < n && a[start + step] <= target) {
            start += step;
        }
    }

    if (a[start] == target) {
        return start;
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