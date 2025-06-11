#include <algorithm>
#include <iostream>
#include <vector>

void bubble_sort(std::vector<int>& a) {
    int n = a.size();
    for (int i = 0; i < n - 1; ++i) {
        bool sorted = true;
        for (int j = 0; j < n - 1 - i; ++j) {
            if (a[j] > a[j + 1]) {
                std::swap(a[j], a[j + 1]);
                sorted = false;
            }
        }
        if (sorted) {
            break;
        }
    }
}

int main() {
    int n;

    std::cin >> n;

    std::vector<int> arr(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    bubble_sort(arr);
    for (int i = 0; i < n; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << '\n';
    return 0;
}