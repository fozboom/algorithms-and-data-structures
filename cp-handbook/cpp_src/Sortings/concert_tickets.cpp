#include <iostream>
#include <set>
 
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
 
    int n;
    int m;
 
    std::cin >> n >> m;
 
    std::multiset<int> tickets;
    for (int i = 0; i < n; ++i) {
        int price;
        std::cin >> price;
        tickets.insert(price);
    }
 
    for (int i = 0; i < m; ++i) {
        int max_price;
        std::cin >> max_price;
 
        auto it = tickets.upper_bound(max_price);
 
        if (it == tickets.begin()) {
            std::cout << -1 << "\n";
        }
 
        else {
            --it;
 
            std::cout << *it << "\n";
 
            tickets.erase(it);
        }
    
    }
}