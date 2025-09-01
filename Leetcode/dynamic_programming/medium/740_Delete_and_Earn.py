from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_element = max(nums)
        points = [0] * (max_element + 1)

        for num in nums:
            points[num] += num

        dp = [None] * (max_element + 1)

        dp[0] = points[0]
        dp[1] = points[1]

        for i in range(2, max_element + 1):
            dp[i] = max(points[i] + dp[i - 2], dp[i - 1])

        return dp[max_element]
