#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {  // NOLINT
        unordered_map<int, int> map;
        vector<int> result;

        for (int i = 0; i < nums.size(); ++i) {
            int to_add = target - nums[i];

            if (map.find(to_add) != map.end()) {
                result = {i, map[to_add]};
                break;
            }

            map[nums[i]] = i;
        }
        return result;
    }
};