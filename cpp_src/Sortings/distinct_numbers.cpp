#include <iostream>
#include <set>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);

    std::set<int> st;
    int n;
    
    std::cin >> n;
    while (n--)
    {
        int x;
        std::cin >> x;
        st.emplace(x);
    }
    std::cout << st.size() << "\n";
    return 0;
}