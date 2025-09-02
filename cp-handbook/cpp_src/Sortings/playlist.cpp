#include <iostream>
#include <vector>
#include <set>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int n;
    std::cin >> n;

    std::vector<int> k(n);
    for (int i = 0; i < n; i++) {
        std::cin >> k[i];
    }

    int left = 0;
    std::multiset<int> unique_songs;

    int max_length = 0;
    for (int right = 0; right < n; right++) {
        while (bool(unique_songs.count(k[right]))) {
            unique_songs.erase(unique_songs.find(k[left]));
            left++;
        }
        max_length = std::max(max_length, right - left + 1);
        unique_songs.insert(k[right]);
    }

    std::cout << max_length << std::endl;
    return 0;
}