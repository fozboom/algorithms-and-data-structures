#include <cassert>
#include <vector>
using namespace std;
class Solution {
   public:
    int tribonacci(int n) {  // NOLINT
        vector<int> dp(n + 1);
        if (n == 0) {
            return 0;
        }

        if (n == 1 || n == 2) {
            return 1;
        }

        dp[0] = 0;
        dp[1] = dp[2] = 1;

        for (int i = 3; i < n + 1; ++i) {               // NOLINT
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];  // NOLINT
        }
        return dp[n];
    }
};

int main() {
    Solution solution;
    assert(solution.tribonacci(4) == 4);
    assert(solution.tribonacci(5) == 7);
    return 0;
}