class Solution(object):
    def climbStairs(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        steps = [None] * (n + 1)

        steps[0] = steps[1] = 1

        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[n]
