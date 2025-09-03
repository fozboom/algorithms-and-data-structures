#include <cassert>
#include <vector>
using namespace std;
class Solution {
   public:
    int climbStairs(int n) {  // NOLINT
        vector<int> dp(n + 1);

        dp[0] = dp[1] = 1;

        for (int i = 2; i < n + 1; ++i) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
};

int main() {
    Solution sol;
    assert(sol.climbStairs(5) == 8);
    assert(sol.climbStairs(3) == 3);
    assert(sol.climbStairs(2) == 2);
    assert(sol.climbStairs(1) == 1);

    return 0;
}