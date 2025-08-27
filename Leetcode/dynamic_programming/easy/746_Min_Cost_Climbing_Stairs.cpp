#include <algorithm>
#include <cassert>
#include <vector>
using namespace std;
class Solution {
   public:
    static int MinCostClimbingStairs(vector<int>& cost) {
        vector<int> prices(cost.size() + 1);
        prices[0] = prices[1] = 0;

        for (int i = 2; i < prices.size(); ++i) {
            prices[i] = min(prices[i - 2] + cost[i - 2], prices[i - 1] + cost[i - 1]);
        }
        return prices.back();
    }
};

int main() {
    vector<int> cost1 = {10, 15, 20};  // NOLINT
    int result = Solution::MinCostClimbingStairs(cost1);
    assert(result == 15);

    vector<int> cost2 = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};  // NOLINT
    result = Solution::MinCostClimbingStairs(cost2);
    assert(result == 6);

    return 0;
}