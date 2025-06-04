#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);

    int n, m, k;

    std::cin >> n >> m >> k;

    std::vector<int> a(n);
    std::vector<int> b(m);

    for (int i = 0; i < n; ++i)
    {
        std::cin >> a[i];
    }

    for (int i = 0; i < m; ++i)
    {
        std::cin >> b[i];
    }

    std::sort(a.begin(), a.end());
    std::sort(b.begin(), b.end());

    int count = 0;
    int i = 0, j = 0;
    
    while (i < n && j < m) {
        if (abs(a[i] - b[j]) <= k) {
            count++;
            i++;
            j++;
        } else if (a[i] < b[j]) {
            i++;
        } else {
            j++;
        }
    }

    std::cout << count;
}