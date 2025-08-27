#include <cassert>
#include <vector>

class Solution {
   public:
    static int Fib(int n) {
        if (n == 0) {
            return 0;
        }

        std::vector<int> num(n + 1);
        num[0] = 0;
        num[1] = 1;

        for (int i = 2; i < n + 1; i++) {
            num[i] = num[i - 1] + num[i - 2];
        }

        return num[n];
    }
};

int main() {
    const int kTest1 = 5;
    int result = Solution::Fib(kTest1);
    assert(result == 5);

    const int kTest2 = 2;
    result = Solution::Fib(kTest2);
    assert(result == 1);

    return 0;
}