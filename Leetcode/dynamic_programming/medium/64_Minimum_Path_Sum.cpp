#include <algorithm>
#include <cstddef>
// #include <iostream>
#include <vector>

using namespace std;
class Solution {
   public:
    static int MinPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size()));

        dp[0][0] = grid[0][0];

        for (size_t i = 1; i < m; ++i) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }

        for (size_t j = 1; j < n; ++j) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        for (size_t i = 1; i < m; ++i) {
            for (size_t j = 1; j < n; ++j) {
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        // Print2DVector(dp);
        return dp[m - 1][n - 1];
    }

    // static void Print2DVector(const vector<vector<int>>& vec) {
    //     for (const auto& row : vec) {
    //         for (const auto& el : row) {
    //             cout << el << ' ';
    //         }
    //         cout << '\n';
    //     }
    // }
};

int main() {
    vector<vector<int>> grid = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};  // NOLINT
    Solution::MinPathSum(grid);
}