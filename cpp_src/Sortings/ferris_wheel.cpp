#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);

    int n;
    int x;

    std::cin >> n >> x;

    std::vector<int> p(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> p[i];
    }

    std::sort(p.begin(), p.end());

    int left = 0;
    int right = p.size() - 1;
    int gondolas = 0;

    while (left <= right) {
        if (left == right) {
            gondolas += 1;
            break;
        }

        if (p[left] + p[right] <= x) {
            gondolas += 1;
            left += 1;
            right -= 1;
        } else {
            gondolas += 1;
            right -= 1;
        }
    }

    std::cout << gondolas;
}