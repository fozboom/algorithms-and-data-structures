
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;
class Solution {
   public:
    static int Rob(vector<int>& nums) {
        const int kSize = nums.size();
        if (nums.size() == 1) {
            return nums[0];
        }

        if (nums.size() == 2) {
            return max(nums[0], nums[1]);
        }

        vector<int> result(nums.size());

        result[0] = nums[0];
        result[1] = nums[1];
        result[2] = nums[2] + nums[0];

        for (int i = 3; i < result.size(); ++i) {                               // NOLINT
            result[i] = max(nums[i] + result[i - 2], nums[i] + result[i - 3]);  // NOLINT
        }

        return max(result[kSize - 1], result[kSize - 2]);
    }
};

int main() {
    vector<int> test = {2, 7, 100, 3, 15, 39, 7, 9, 23, 1};  // NOLINT
    vector<int> test2 = {2, 7, 9, 3, 1};                     // NOLINT

    assert(Solution::Rob(test) == 164);
    assert(Solution::Rob(test2) == 12);
}
